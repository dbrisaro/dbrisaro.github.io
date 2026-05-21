"""
Generate WOA18 temperature maps for the water masses story map.
Outputs:
  img/temp_surface.png   — annual mean temperature at 0 m
  img/temp_1000m.png     — annual mean temperature at 1000 m
"""

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cmocean
import netCDF4 as nc
from pathlib import Path

OUT = Path(__file__).parent / "img"
OUT.mkdir(exist_ok=True)

WOA_T = (
    "https://www.ncei.noaa.gov/thredds-ocean/dodsC/ncei/woa/temperature"
    "/decav/1.00/woa18_decav_t00_01.nc"
)

DEPTHS = {
    "surface": (0,  "Temperatura superficial — media anual (WOA18)",  "temp_surface.png"),
    "1000m":   (46, "Temperatura a 1000 m — media anual (WOA18)",     "temp_1000m.png"),
}

VMIN, VMAX = -2, 30      # surface range
VMIN_D, VMAX_D = -2, 10  # deep range


def make_map(ax, data, lat, lon, vmin, vmax, title, depth_label):
    cmap = cmocean.cm.thermal

    proj = ccrs.Robinson(central_longitude=-30)
    ax = plt.axes(ax.get_position(), projection=proj)

    ax.set_global()

    # filled contour
    lon2d, lat2d = np.meshgrid(lon, lat)
    cf = ax.pcolormesh(
        lon2d, lat2d, data,
        transform=ccrs.PlateCarree(),
        cmap=cmap, vmin=vmin, vmax=vmax,
        shading="auto", rasterized=True
    )

    # land
    ax.add_feature(cfeature.LAND, facecolor="#2d2d2d", zorder=2)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.4, edgecolor="#555", zorder=3)

    # gridlines
    gl = ax.gridlines(
        draw_labels=False, linewidth=0.3,
        color="white", alpha=0.25, linestyle="--"
    )
    gl.xlocator = mticker.FixedLocator(range(-180, 181, 60))
    gl.ylocator = mticker.FixedLocator([-60, -30, 0, 30, 60])

    # colorbar
    cbar = plt.colorbar(cf, ax=ax, orientation="horizontal",
                        pad=0.04, fraction=0.03, shrink=0.7, aspect=30)
    cbar.set_label("°C", fontsize=9, color="white")
    cbar.ax.tick_params(colors="white", labelsize=8)
    cbar.outline.set_edgecolor("white")

    # title
    ax.set_title(title, fontsize=11, color="white", pad=8,
                 fontfamily="DejaVu Sans")

    # depth badge
    ax.text(0.02, 0.05, depth_label, transform=ax.transAxes,
            fontsize=9, color="white", alpha=0.8,
            fontfamily="DejaVu Sans",
            bbox=dict(boxstyle="round,pad=0.3", fc="black", alpha=0.4, ec="none"))

    return cf


print("Conectando a WOA18 …")
ds = nc.Dataset(WOA_T)
lat = ds["lat"][:]
lon = ds["lon"][:]
t_surf = np.ma.masked_invalid(ds["t_an"][0, 0, :, :])   # depth index 0 → 0 m
t_1000 = np.ma.masked_invalid(ds["t_an"][0, 46, :, :])  # depth index 46 → 1000 m
ds.close()
print("Datos descargados.")

BG = "#0a1628"

for key, (idx, title, fname) in DEPTHS.items():
    data = t_surf if key == "surface" else t_1000
    vmin = VMIN if key == "surface" else VMIN_D
    vmax = VMAX if key == "surface" else VMAX_D
    depth_label = "0 m (superficie)" if key == "surface" else "1 000 m de profundidad"

    fig = plt.figure(figsize=(12, 6), facecolor=BG)
    ax_dummy = fig.add_axes([0.03, 0.08, 0.94, 0.88])
    ax_dummy.set_visible(False)

    cf = make_map(ax_dummy, data, lat, lon, vmin, vmax, title, depth_label)

    outpath = OUT / fname
    fig.savefig(outpath, dpi=150, bbox_inches="tight",
                facecolor=BG, edgecolor="none")
    plt.close(fig)
    print(f"  → {outpath}")

print("Listo.")
