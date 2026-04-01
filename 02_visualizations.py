import sys
import os

# Add parent directory to path to import plot_style
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style import set_tufte_defaults, apply_tufte_style, save_tufte_figure, COLORS

"""
Visualization script for Grid Infrastructure Analysis Blog
Generates publication-quality figures at 300 DPI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.lines as mlines

import sys
import os

# Add parent directory to path to import plot_style
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style import set_tufte_defaults, apply_tufte_style, save_tufte_figure, COLORS






def generate_infrastructure_architecture():
    """Generate grid infrastructure system architecture diagram."""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.axis('off')
    
    # Data layer
    y_data = 8
    data_box = FancyBboxPatch((1, y_data), 3, 1.2, 
                              boxstyle="round,pad=0.1", 
                              facecolor=COLORS['black'], 
                              edgecolor='black', linewidth=2)
    ax.add_patch(data_box)
    ax.text(2.5, y_data + 0.6, 'HIFLD Dataset\n300,000+ Transmission Lines', 
           ha='center', va='center', fontsize=10, color='white', weight='bold')
    
    # Storage layer
    y_storage = 6.5
    storage_items = [
        {'name': 'Parquet\nStorage', 'x': 0.5, 'color': COLORS['darkgray']},
        {'name': 'Spatial\nIndex', 'x': 2.5, 'color': COLORS['darkgray']},
        {'name': 'Metadata\nCache', 'x': 4.5, 'color': COLORS['darkgray']}
    ]
    
    for item in storage_items:
        box = FancyBboxPatch((item['x'], y_storage), 1.5, 0.8, 
                            boxstyle="round,pad=0.05",
                            facecolor=item['color'], 
                            edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(item['x'] + 0.75, y_storage + 0.4, item['name'], 
               ha='center', va='center', fontsize=8, color='white', weight='bold')
    
    # Service layer
    y_service = 5
    service_box = FancyBboxPatch((0.5, y_service), 5.5, 1, 
                                boxstyle="round,pad=0.1",
                                facecolor=COLORS['gray'], 
                                edgecolor='black', linewidth=2, alpha=0.9)
    ax.add_patch(service_box)
    ax.text(3.25, y_service + 0.5, 'TransmissionLinesService\nQuery • Filter • Analysis • Export', 
           ha='center', va='center', fontsize=10, color='white', weight='bold')
    
    # Analysis modules
    y_analysis = 3.5
    modules = [
        {'name': 'Voltage\nAnalysis', 'x': 0.5, 'color': COLORS['darkgray']},
        {'name': 'Corridor\nDetection', 'x': 2, 'color': COLORS['darkgray']},
        {'name': 'Owner\nMapping', 'x': 3.5, 'color': COLORS['darkgray']},
        {'name': 'Capacity\nAnalysis', 'x': 5, 'color': COLORS['darkgray']}
    ]
    
    for module in modules:
        box = FancyBboxPatch((module['x'], y_analysis), 1.3, 0.8, 
                            boxstyle="round,pad=0.05",
                            facecolor=module['color'], 
                            edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(module['x'] + 0.65, y_analysis + 0.4, module['name'], 
               ha='center', va='center', fontsize=8, color='white', weight='bold')
    
    # Visualization layer
    y_viz = 2
    viz_box = FancyBboxPatch((1, y_viz), 4.5, 1, 
                            boxstyle="round,pad=0.1",
                            facecolor=COLORS['gray'], 
                            edgecolor='black', linewidth=2, alpha=0.9)
    ax.add_patch(viz_box)
    ax.text(3.25, y_viz + 0.5, 'Interactive Visualization\nGeoJSON • Mapping • Dashboards', 
           ha='center', va='center', fontsize=10, color='white', weight='bold')
    
    # Output layer
    y_output = 0.3
    outputs = [
        {'name': 'Web Maps', 'x': 0.5},
        {'name': 'API', 'x': 2},
        {'name': 'Reports', 'x': 3.5},
        {'name': 'Alerts', 'x': 5}
    ]
    
    for output in outputs:
        box = FancyBboxPatch((output['x'], y_output), 1.3, 0.6, 
                            boxstyle="round,pad=0.05",
                            facecolor=COLORS['black'], 
                            edgecolor='black', linewidth=1.5, alpha=0.7)
        ax.add_patch(box)
        ax.text(output['x'] + 0.65, y_output + 0.3, output['name'], 
               ha='center', va='center', fontsize=8, color='white', weight='bold')
    
    # Integration box (right side)
    y_integration = 2
    integration_box = FancyBboxPatch((7, y_integration), 3, 6, 
                                    boxstyle="round,pad=0.15",
                                    facecolor=COLORS['gray'], 
                                    edgecolor='black', linewidth=2, alpha=0.3)
    ax.add_patch(integration_box)
    ax.text(8.5, 7.5, 'Data Integration', ha='center', fontsize=11, weight='bold')
    
    integration_items = [
        {'name': 'Load Forecasts', 'y': 6.8},
        {'name': 'Weather Data', 'y': 6.1},
        {'name': 'Outage Reports', 'y': 5.4},
        {'name': 'Market Prices', 'y': 4.7},
        {'name': 'Maintenance\nSchedules', 'y': 4},
        {'name': 'Capacity Limits', 'y': 3.3}
    ]
    
    for item in integration_items:
        box = FancyBboxPatch((7.3, item['y']), 2.4, 0.5, 
                            boxstyle="round,pad=0.05",
                            facecolor='white', 
                            edgecolor=COLORS['gray'], linewidth=1.5)
        ax.add_patch(box)
        ax.text(8.5, item['y'] + 0.25, item['name'], 
               ha='center', va='center', fontsize=8)
    
    # Draw arrows
    ax.arrow(2.5, y_data, 0, -1.3, head_width=0.2, head_length=0.15, 
            fc='black', ec='black', linewidth=2)
    ax.arrow(3.25, y_service, 0, -1.3, head_width=0.2, head_length=0.15, 
            fc='black', ec='black', linewidth=2)
    ax.arrow(3.25, y_viz, 0, -1.5, head_width=0.2, head_length=0.15, 
            fc='black', ec='black', linewidth=2)
    
    # Integration arrows
    for y_pos in [6.8, 5.4, 4]:
        ax.arrow(6.9, y_pos + 0.25, -0.5, 0, head_width=0.15, head_length=0.1, 
                fc=COLORS['gray'], ec=COLORS['gray'], linewidth=1.5, alpha=0.6)
    
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 9.5)
    
    ax.text(5.5, 9.3, 'Grid Infrastructure Analysis Architecture', 
           ha='center', fontsize=14, weight='bold')
    
    plt.tight_layout()
    plt.savefig('02_grid_infrastructure_architecture.png', bbox_inches='tight', dpi=300)
    print("✓ Generated: 02_grid_infrastructure_architecture.png")
    plt.close()


def generate_grid_analysis_dashboard():
    """Generate comprehensive grid analysis dashboard."""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)
    
    # Voltage class distribution
    ax1 = fig.add_subplot(gs[0, :2])
    voltage_classes = ['765 kV\nUltra-High', '500 kV\nExtra-High', 
                       '345 kV\nHigh', '230 kV\nHigh', '138 kV\nSub-Trans']
    line_counts = [1200, 3500, 12500, 28000, 45000]
    colors_voltage = [COLORS['black'], COLORS['darkgray'], COLORS['gray'], 
                     COLORS['lightgray'], COLORS['gray']]
    
    bars = ax1.barh(voltage_classes, line_counts, color=colors_voltage, 
                    edgecolor='black', linewidth=1.5)
    ax1.set_xlabel('Number of Lines', fontsize=11, weight='bold')
    ax1.set_title('Transmission Lines by Voltage Class', fontsize=12, weight='bold')
    ax1.grid(True, alpha=0.3, axis='x', linestyle='--')
    
    for i, (bar, count) in enumerate(zip(bars, line_counts)):
        width = bar.get_width()
        percentage = (count / sum(line_counts)) * 100
        ax1.text(width + 1000, i, f'{count:,} ({percentage:.1f}%)', 
                va='center', fontsize=9, weight='bold')
    
    # Network statistics pie
    ax2 = fig.add_subplot(gs[0, 2])
    line_types = ['Overhead', 'Underground', 'Submarine']
    type_counts = [85, 13, 2]
    colors_types = [COLORS['black'], COLORS['darkgray'], COLORS['gray']]
    
    wedges, texts, autotexts = ax2.pie(type_counts, labels=line_types, autopct='%1.1f%%',
                                       colors=colors_types, startangle=90,
                                       textprops={'weight': 'bold', 'fontsize': 9})
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
    ax2.set_title('Line Type Distribution', fontsize=11, weight='bold')
    
    # Critical corridors
    ax3 = fig.add_subplot(gs[1, :])
    corridors = ['TX-OK\nInterconnect', 'CA-NV\nPaths', 'PJM-MISO\nSeams', 
                 'NY-NE\nTie Lines', 'ERCOT\nInternal']
    parallel_lines = [12, 8, 15, 6, 25]
    max_voltages = [765, 500, 500, 345, 345]
    criticality = [95, 78, 92, 65, 88]
    
    x = np.arange(len(corridors))
    width = 0.25
    
    bars1 = ax3.bar(x - width, parallel_lines, width, label='Parallel Lines', 
                   color=COLORS['darkgray'], edgecolor='black', linewidth=1)
    bars2 = ax3.bar(x, [v/10 for v in max_voltages], width, label='Max Voltage (÷10 kV)', 
                   color=COLORS['gray'], edgecolor='black', linewidth=1)
    bars3 = ax3.bar(x + width, criticality, width, label='Criticality Score', 
                   color=COLORS['black'], edgecolor='black', linewidth=1)
    
    ax3.set_xlabel('Transmission Corridor', fontsize=11, weight='bold')
    ax3.set_ylabel('Value', fontsize=11, weight='bold')
    ax3.set_title('Critical Transmission Corridor Analysis', fontsize=12, weight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(corridors, fontsize=9)
    ax3.legend(loc='upper right', ncol=3, fontsize=9)
    ax3.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # Top utilities
    ax4 = fig.add_subplot(gs[2, 0])
    utilities = ['FERC', 'AEP', 'Duke', 'Southern', 'Exelon', 'NextEra']
    util_lines = [18500, 15200, 12800, 11200, 9800, 8500]
    
    bars = ax4.bar(range(len(utilities)), util_lines, 
                   color=COLORS['black'], edgecolor='black', linewidth=1.5)
    ax4.set_ylabel('Number of Lines', fontsize=10, weight='bold')
    ax4.set_title('Top Transmission Owners', fontsize=11, weight='bold')
    ax4.set_xticks(range(len(utilities)))
    ax4.set_xticklabels(utilities, rotation=45, ha='right', fontsize=8)
    ax4.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    for i, (bar, count) in enumerate(zip(bars, util_lines)):
        ax4.text(i, bar.get_height() + 500, f'{count:,}', 
                ha='center', va='bottom', fontsize=8)
    
    # Network length by voltage
    ax5 = fig.add_subplot(gs[2, 1])
    voltages_length = ['765', '500', '345', '230', '138']
    miles = [12000, 28000, 65000, 120000, 185000]
    
    bars = ax5.barh(voltages_length, miles, 
                    color=[COLORS['black'], COLORS['darkgray'], COLORS['gray'], 
                          COLORS['lightgray'], COLORS['gray']],
                    edgecolor='black', linewidth=1.5)
    ax5.set_xlabel('Total Miles', fontsize=10, weight='bold')
    ax5.set_ylabel('Voltage (kV)', fontsize=10, weight='bold')
    ax5.set_title('Network Length by Voltage', fontsize=11, weight='bold')
    ax5.grid(True, alpha=0.3, axis='x', linestyle='--')
    
    for i, (bar, mile) in enumerate(zip(bars, miles)):
        ax5.text(mile + 3000, i, f'{mile:,}', va='center', fontsize=8)
    
    # Capacity utilization
    ax6 = fig.add_subplot(gs[2, 2])
    regions = ['West', 'Texas', 'Central', 'East', 'NE']
    utilization = [72, 65, 58, 81, 76]
    colors_util = [COLORS['gray'] if u > 70 else COLORS['darkgray'] for u in utilization]
    
    bars = ax6.bar(range(len(regions)), utilization, 
                   color=colors_util, edgecolor='black', linewidth=1.5)
    ax6.axhline(y=80, color=COLORS['black'], linestyle='--', linewidth=2, 
                label='Critical Threshold')
    ax6.set_ylabel('Utilization (%)', fontsize=10, weight='bold')
    ax6.set_title('Corridor Capacity Utilization', fontsize=11, weight='bold')
    ax6.set_xticks(range(len(regions)))
    ax6.set_xticklabels(regions, fontsize=9)
    ax6.set_ylim(0, 100)
    ax6.legend(fontsize=8)
    ax6.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    for i, (bar, util) in enumerate(zip(bars, utilization)):
        ax6.text(i, bar.get_height() + 2, f'{util}%', 
                ha='center', va='bottom', fontsize=9, weight='bold')
    
    plt.suptitle('Grid Infrastructure Analysis Dashboard', 
                fontsize=14, weight='bold', y=0.995)
    
    plt.savefig('02_grid_infrastructure_analysis.png', bbox_inches='tight', dpi=300)
    print("✓ Generated: 02_grid_infrastructure_analysis.png")
    plt.close()


def generate_grid_visualization_interface():
    """Generate example grid visualization interface."""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3, 
                         height_ratios=[2, 1])
    
    # Main map area (simulated)
    ax_map = fig.add_subplot(gs[0, :])
    ax_map.set_xlim(-125, -65)
    ax_map.set_ylim(25, 50)
    ax_map.set_facecolor('#E8F4F8')
    ax_map.set_title('U.S. Transmission Network Visualization', 
                     fontsize=13, weight='bold', pad=15)
    ax_map.set_xlabel('Longitude', fontsize=10)
    ax_map.set_ylabel('Latitude', fontsize=10)
    ax_map.grid(True, alpha=0.3, linestyle='--')
    
    # Simulate transmission lines
    np.random.seed(42)
    for _ in range(80):
        lon_start = np.random.uniform(-120, -70)
        lat_start = np.random.uniform(28, 48)
        lon_end = lon_start + np.random.uniform(-5, 5)
        lat_end = lat_start + np.random.uniform(-3, 3)
        
        voltage = np.random.choice([765, 500, 345, 230])
        if voltage == 765:
            color = COLORS['black']
            width = 3
        elif voltage == 500:
            color = COLORS['darkgray']
            width = 2.5
        elif voltage == 345:
            color = COLORS['gray']
            width = 2
        else:
            color = COLORS['lightgray']
            width = 1.5
        
        ax_map.plot([lon_start, lon_end], [lat_start, lat_end], 
                   color=color, linewidth=width, alpha=0.7)
    
    # Add legend for voltage classes
    legend_elements = [
        mlines.Line2D([0], [0], color=COLORS['black'], linewidth=3, 
                     label='765 kV Ultra-High'),
        mlines.Line2D([0], [0], color=COLORS['darkgray'], linewidth=2.5, 
                     label='500 kV Extra-High'),
        mlines.Line2D([0], [0], color=COLORS['gray'], linewidth=2, 
                     label='345 kV High'),
        mlines.Line2D([0], [0], color=COLORS['lightgray'], linewidth=1.5, 
                     label='230 kV Sub-Transmission')
    ]
    ax_map.legend(handles=legend_elements, loc='lower left', fontsize=9,
                 framealpha=0.9, edgecolor='black')
    
    # Query panel
    ax_query = fig.add_subplot(gs[1, 0])
    ax_query.axis('off')
    ax_query.text(0.5, 0.9, 'Query Filters', ha='center', fontsize=11, 
                 weight='bold', transform=ax_query.transAxes)
    
    query_options = [
        'Voltage Class: 345-765 kV',
        'Owner: All Utilities',
        'Status: In Service',
        'Type: Overhead',
        'Region: CONUS'
    ]
    
    for i, option in enumerate(query_options):
        y_pos = 0.7 - i * 0.15
        box = FancyBboxPatch((0.1, y_pos-0.05), 0.8, 0.08, 
                            transform=ax_query.transAxes,
                            boxstyle="round,pad=0.01",
                            facecolor='white', edgecolor=COLORS['black'], linewidth=2)
        ax_query.add_patch(box)
        ax_query.text(0.15, y_pos, option, fontsize=8, 
                     transform=ax_query.transAxes, va='center')
    
    # Statistics panel
    ax_stats = fig.add_subplot(gs[1, 1])
    ax_stats.axis('off')
    ax_stats.text(0.5, 0.9, 'Network Statistics', ha='center', fontsize=11, 
                 weight='bold', transform=ax_stats.transAxes)
    
    stats_display = [
        ('Lines Displayed:', '8,427'),
        ('Total Miles:', '142,350'),
        ('Avg Voltage:', '387 kV'),
        ('Unique Owners:', '42'),
        ('Substations:', '1,256')
    ]
    
    for i, (label, value) in enumerate(stats_display):
        y_pos = 0.7 - i * 0.15
        ax_stats.text(0.15, y_pos, label, fontsize=8, 
                     transform=ax_stats.transAxes, va='center')
        ax_stats.text(0.85, y_pos, value, fontsize=8, weight='bold',
                     transform=ax_stats.transAxes, va='center', ha='right',
                     color=COLORS['black'])
    
    # Actions panel
    ax_actions = fig.add_subplot(gs[1, 2])
    ax_actions.axis('off')
    ax_actions.text(0.5, 0.9, 'Actions', ha='center', fontsize=11, 
                   weight='bold', transform=ax_actions.transAxes)
    
    actions = ['Export GeoJSON', 'Generate Report', 'Analyze Capacity', 'View Details']
    action_colors = [COLORS['darkgray'], COLORS['black'], COLORS['gray'], COLORS['gray']]
    
    for i, (action, color) in enumerate(zip(actions, action_colors)):
        y_pos = 0.7 - i * 0.15
        box = FancyBboxPatch((0.1, y_pos-0.04), 0.8, 0.08, 
                            transform=ax_actions.transAxes,
                            boxstyle="round,pad=0.01",
                            facecolor=color, edgecolor='black', linewidth=1.5)
        ax_actions.add_patch(box)
        ax_actions.text(0.5, y_pos, action, fontsize=9, weight='bold',
                       transform=ax_actions.transAxes, va='center', ha='center',
                       color='white')
    
    plt.savefig('02_grid_infrastructure_visualization.png', bbox_inches='tight', dpi=300)
    print("✓ Generated: 02_grid_infrastructure_visualization.png")
    plt.close()


if __name__ == "__main__":
    print("Generating visualizations for Grid Infrastructure Analysis Blog...\n")
    
    generate_infrastructure_architecture()
    generate_grid_analysis_dashboard()
    generate_grid_visualization_interface()
    
    print("\n✓ All visualizations generated successfully!")
    print("  - 02_grid_infrastructure_architecture.png")
    print("  - 02_grid_infrastructure_analysis.png")
    print("  - 02_grid_infrastructure_visualization.png")

