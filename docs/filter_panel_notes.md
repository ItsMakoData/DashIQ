# DashIQ — Sidebar Filter Panel

## Objective
To enable interactive filtering for dashboard analysis and support dynamic data exploration.

---

## Filters Implemented

### 1. **Date Range Filter** 📅
- **Column:** Order Date
- **Type:** Date Range Picker
- **Behavior:** Filters all data between selected start and end dates
- **Default:** Min to Max date in dataset

### 2. **Region Filter** 🌍
- **Column:** Region
- **Type:** Multi-select
- **Behavior:** Shows all unique regions, allows multiple selections
- **Default:** All regions selected

### 3. **Category Filter** 📦
- **Column:** Item Type
- **Type:** Multi-select
- **Behavior:** Shows all unique categories, allows multiple selections
- **Default:** All categories selected

### 4. **Product Filter** 🛒
- **Column:** Item Type (Dependent)
- **Type:** Multi-select (Dynamic)
- **Behavior:** Filtered based on selected categories
- **Special Feature:** Only shows products from selected categories

---

## Key Features

✅ **Dynamic Filtering**
- All KPIs, charts, and data tables update in real-time based on filter selections
- Uses `filtered_df` throughout the app instead of raw `df`

✅ **Dependent Filtering**
- Product filter automatically updates based on selected categories
- Prevents invalid filter combinations

✅ **Empty Data Handling**
- Gracefully handles scenarios where filters result in no data
- Displays warning message and prevents errors

✅ **Reset Functionality**
- "Reset Filters" button resets all selections to defaults
- Uses `st.rerun()` for immediate effect

✅ **Active Filters Display**
- Shows current filter selections to users
- Improves transparency and helps with debugging

---

## Implementation Details

### Filter Logic Flow
1. Load data and convert `Order Date` to datetime
2. Create sidebar header and filter controls
3. Build `filtered_df` by applying all filters sequentially:
   - Date range filter
   - Region filter
   - Category filter
   - Product filter (dependent on category)
4. Check if `filtered_df` is empty
5. Calculate KPIs using `filtered_df`
6. Display active filters and sample data from `filtered_df`

### Zero Division Protection
- Profit margin calculation includes check: `if total_revenue != 0 else 0`
- Prevents errors when revenue is zero

### Data Persistence
- Date conversion happens once at load time
- Filters create new dataframe copy to avoid modifying original data
- All calculations use filtered data for consistency

---

## User Experience

### Workflow
1. User opens dashboard
2. All filters default to showing all data
3. User adjusts filters in sidebar
4. Dashboard content updates dynamically
5. Active filters are displayed for reference
6. User can reset to default state with one click

### Performance
- Uses Streamlit's caching for initial data load
- Multi-select controls update efficiently
- No unnecessary recalculations

---

## Result
The dashboard now supports user-driven exploration and provides a professional BI experience with dynamic, responsive filtering.
