# ALT_SEL_CAT

> Used to store alternate search categories or items. (i.e. PowerOrders favorites and favorite folders)

**Description:** Alternate Orderable Selection Category  
**Table type:** REFERENCE  
**Primary key:** `ALT_SEL_CATEGORY_ID`  
**Columns:** 19  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADHOC_IND` | DOUBLE |  |  | Indicates this category is for Ad hoc charting from the task list. |
| 2 | `AHFS_IND` | DOUBLE |  |  | Used to mark a category or item as a therapeutic class or category. |
| 3 | `ALT_SEL_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Primary key for this table. |
| 4 | `CHILD_CAT_IND` | DOUBLE |  |  | Indicates that this category has child categories. |
| 5 | `FOLDER_FLAG` | DOUBLE |  |  | Type of Folder related to the corresponding Alternate Selection Category; i.e., 1 - Normal Folder, 2 - IV Favorite Folder |
| 6 | `IV_SET_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | This ID uniquely identifies the IV set used to place the order. This field is only valued for IV orders that start with an IV set. |
| 7 | `LONG_DESCRIPTION` | VARCHAR(1000) |  |  | Long description string for this category. |
| 8 | `LONG_DESCRIPTION_KEY_CAP` | VARCHAR(1000) |  |  | The Long Description column stored in all uppercase with spaces & special characters removed. |
| 9 | `LONG_DESCRIPTION_KEY_CAP_A_NLS` | VARCHAR(4000) |  |  | Stores the corresponding non-English character set values for the Long_Description_Key_CAP column. Used to sort correctly internationally. |
| 10 | `LONG_DESCRIPTION_KEY_CAP_NLS` | VARCHAR(2002) |  |  | An _NLS sort column for internationalization.Column is no longer used. Replaced by A_NLS column so the French Accent is handled properly. Obsolete. |
| 11 | `OWNER_ID` | DOUBLE | NOT NULL |  | Person ID of the user that created this category. |
| 12 | `SECURITY_FLAG` | DOUBLE |  |  | Used to mark a category or item as private or public writable. 1 - Private, 0 or 2 Public. |
| 13 | `SHORT_DESCRIPTION` | VARCHAR(500) |  |  | Display value to be seen in most apps for this category. |
| 14 | `SOURCE_COMPONENT_FLAG` | DOUBLE | NOT NULL |  | Stores the Source application/task to enable selective display of favorites. 0 - Favorite is not application specific, 1 - Favorite was created in Power Orders, 2 - Favorite was created in Easy Script, 3 - Favorite was created in Super Bill. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IV_SET_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `ALT_SEL_CATEGORY_ID` |
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `CHILD_ALT_SEL_CAT_ID` |
| [BR_OF_PARENT_RELTN](BR_OF_PARENT_RELTN.md) | `ALT_SEL_CATEGORY_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `THER_CLASS_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `PARENT_THERAP_CLASS_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `ROOT_THERAP_CLASS_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `THERAP_CLASS_ID` |
| [SCH_APPT_ORD](SCH_APPT_ORD.md) | `ALT_SEL_CATEGORY_ID` |

