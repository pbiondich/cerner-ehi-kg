# DA_LOGICAL_VIEW

> Contains the definitions of logical views fused in Discern Analytics 2.0 metadata.

**Description:** Discern Analytics Logical View  
**Table type:** REFERENCE  
**Primary key:** `DA_LOGICAL_VIEW_ID`  
**Columns:** 18  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this logical view was created by Cerner. |
| 3 | `DA_LOGICAL_VIEW_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the DA_LOGICAL_VIEW table. |
| 4 | `DEPRECATED_IND` | DOUBLE | NOT NULL |  | Indicates this logical view has been deprecated. A row that has been deprecated indicates that there is a future intention to inactivate the row. |
| 5 | `EXTENDED_IND` | DOUBLE | NOT NULL |  | Indicates a Cerner created logical view has been modified by a user. |
| 6 | `LOGICAL_VIEW_DESC` | VARCHAR(255) | NOT NULL |  | A description of the logical view. |
| 7 | `LOGICAL_VIEW_NAME` | VARCHAR(100) | NOT NULL |  | The name of the logical view. |
| 8 | `LOGICAL_VIEW_NAME_KEY` | VARCHAR(100) | NOT NULL |  | The name of the logical view, uppercased and white space removed, for use in searching. |
| 9 | `LOGICAL_VIEW_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | The NLS key for searching in all non-English locales. |
| 10 | `LOGICAL_VIEW_UUID` | VARCHAR(100) | NOT NULL |  | The UUID is used to establish a unique identifier across all systems. The UUID for an item will be the same from one environment to another. |
| 11 | `OWNER_GROUP_CD` | DOUBLE | NOT NULL |  | The owner group of the logical view, used to categorize items across a solution group or functional area (ex Operational vs Financial). |
| 12 | `PARENT_LOGICAL_VIEW_ID` | DOUBLE | NOT NULL | FK→ | When a logical view contains a parent_logical_view_id, the view referenced as the parent is considered to be inherited. The logical view will thus contain all of the elements, tables, and joins both of the current logical view as well as the parent logical view. Contents of the parent logical view may not be changed through the child logical view. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERSION_TXT` | VARCHAR(50) | NOT NULL |  | Version_txt contains both a major and minor version number. Minor version numbers are auto-updated each time the item is updated, whereas the major version may be updated during the export process. The version_txt is used by the import process to ensure accurate updating across systems. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_LOGICAL_VIEW_ID` | [DA_LOGICAL_VIEW](DA_LOGICAL_VIEW.md) | `DA_LOGICAL_VIEW_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DA_BV_LV_ELEM_RELTN](DA_BV_LV_ELEM_RELTN.md) | `DA_LOGICAL_VIEW_ID` |
| [DA_LOGICAL_VIEW](DA_LOGICAL_VIEW.md) | `PARENT_LOGICAL_VIEW_ID` |
| [DA_LV_TABLE_ELEM_RELTN](DA_LV_TABLE_ELEM_RELTN.md) | `DA_LOGICAL_VIEW_ID` |

