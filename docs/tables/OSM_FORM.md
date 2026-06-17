# OSM_FORM

> Table used to store forms created by the user, usually requisition forms.

**Description:** OSM FORM  
**Table type:** REFERENCE  
**Primary key:** `OSM_FORM_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(100) |  |  | Name or description of Form |
| 3 | `MAX_COL` | DOUBLE |  |  | Maximum Columns allowed for form |
| 4 | `MAX_ROW` | DOUBLE | NOT NULL |  | Maximum Rows allowed for Form |
| 5 | `OSM_FORM_ID` | DOUBLE | NOT NULL | PK | Unique Id used for each Form |
| 6 | `SORT_DIR_FLAG` | DOUBLE | NOT NULL |  | Contains the direction of the sort.1 - Ascending2 - Descending0 - No Sort |
| 7 | `SORT_FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Contains which field type will be used for sorting, 0 for no sort. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [OSM_FORM_GROUPS](OSM_FORM_GROUPS.md) | `OSM_FORM_ID` |
| [OSM_FORM_ORG_GRP_XREF](OSM_FORM_ORG_GRP_XREF.md) | `OSM_FORM_ID` |
| [OSM_FORM_PRINTING](OSM_FORM_PRINTING.md) | `OSM_FORM_ID` |

