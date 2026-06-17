# WORKING_VIEW_SECTION

> Specifies the default definition for working views that are applicable for a given position/location.

**Description:** Specifies the default definition for working views.  
**Table type:** REFERENCE  
**Primary key:** `WORKING_VIEW_SECTION_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | The display name of the section |
| 2 | `EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the child event set name associated to a working view. |
| 3 | `FALLOFF_VIEW_MINUTES` | DOUBLE | NOT NULL |  | ** obsolete ** - this column will no longer be used as of changes made for CR 1-2933021421 - January 2009..Specifies when to remove the event set if it hasn't been documented on within the working view. |
| 4 | `INCLUDED_IND` | DOUBLE | NOT NULL |  | Specifies whether the event set is included on the working view. |
| 5 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Specifies whether the event set is required (for documentation and can't be removed) on the working view. |
| 6 | `SECTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of the section (0=event set; 1=IV Drip) |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WORKING_VIEW_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key |
| 13 | `WORKING_VIEW_SECTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKING_VIEW_ID` | [WORKING_VIEW](WORKING_VIEW.md) | `WORKING_VIEW_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNT_WV_SECTION_KEY](CNT_WV_SECTION_KEY.md) | `DCP_WV_SECTION_REF_ID` |
| [WORKING_VIEW_ITEM](WORKING_VIEW_ITEM.md) | `WORKING_VIEW_SECTION_ID` |

