# SA_REF_CATEGORY

> Contains Records that define the Categories used within the SurgiNet Anesthesia applications. Size - Based on the no. of categories that are built for Meds/Fluids/Params/Items/Actions/Macros. Estimate 100 rows.

**Description:** SA Reference Category  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_CATEGORY_ID`  
**Columns:** 21  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CATEGORY_COLOR` | DOUBLE |  |  | Color associated to the category |
| 6 | `CATEGORY_NAME` | CHAR(50) | NOT NULL |  | Display name of the category |
| 7 | `CATEGORY_NAME_KEY` | VARCHAR(50) |  |  | Display name of the category _KEY FORMAT |
| 8 | `CATEGORY_NAME_KEY_A_NLS` | VARCHAR(200) |  |  | CATEGORY_NAME_KEY_A_NLS column |
| 9 | `CATEGORY_NAME_KEY_NLS` | VARCHAR(102) |  |  | Display name of the category _KEY FORMAT NATIONAL LANGUAGE |
| 10 | `CATEGORY_SEQUENCE` | DOUBLE |  |  | Sequence the category should be displayed in when displayed with the other categories of the same category_type_cd |
| 11 | `CATEGORY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of category the record defines (med, fluid, item, etc.) |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location that this category applies to. 0 for all |
| 13 | `PARENT_SA_REF_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Identifies (if any) the parent category to which this category belongs. If this ID is 0, then this category is not a child of any other category. |
| 14 | `REF_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of reference this item is built for (I.e Anesthesia (0), CVNet(1) |
| 15 | `SA_REF_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Unique value to category record |
| 16 | `SA_REF_ICON_ID` | DOUBLE | NOT NULL | FK→ | Icon to display for category |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_SA_REF_CATEGORY_ID` | [SA_REF_CATEGORY](SA_REF_CATEGORY.md) | `SA_REF_CATEGORY_ID` |
| `SA_REF_ICON_ID` | [SA_REF_ICON](SA_REF_ICON.md) | `SA_REF_ICON_ID` |

## Referenced by (10)

| From table | Column |
|------------|--------|
| [SA_REF_CATEGORY](SA_REF_CATEGORY.md) | `PARENT_SA_REF_CATEGORY_ID` |
| [SA_REF_CAT_ACTION](SA_REF_CAT_ACTION.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_CAT_DEVICE](SA_REF_CAT_DEVICE.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_CAT_FLUID](SA_REF_CAT_FLUID.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_CAT_ITEM](SA_REF_CAT_ITEM.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_CAT_MEDICATION](SA_REF_CAT_MEDICATION.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_CAT_PARAMETER](SA_REF_CAT_PARAMETER.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_CAT_PRSNL](SA_REF_CAT_PRSNL.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_MACRO](SA_REF_MACRO.md) | `SA_REF_CATEGORY_ID` |
| [SA_REF_REQUIRED_CATEGORY](SA_REF_REQUIRED_CATEGORY.md) | `SA_REF_CATEGORY_ID` |

