# SN_RPT_PREFS

> This table holds report preferences (sort order, block utilization parameters, etc.)

**Description:** Holds Report Preferences  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | If this preference has a value that is a foreign key to another table, this will be the foreign key value with the table in the parent_entity_name column. |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the table that this preference has a foreign key to. |
| 3 | `PREFS_STRING` | VARCHAR(255) |  |  | This holds non-foreign key report preference values. |
| 4 | `RPT_FILTER_GRP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key into the SN_RPT_FILTER_GRP table to indicate which filter group this report preference belongs to. |
| 5 | `RPT_PREFS_ID` | DOUBLE | NOT NULL |  | Report Preferences ID. Primary Key |
| 6 | `RPT_PREFS_REF_ID` | DOUBLE | NOT NULL | FK→ | Foreign key into the SN_RPT_PREFS_REF table to indicate what reference this report preference was created from. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RPT_FILTER_GRP_ID` | [SN_RPT_FILTER_GRP](SN_RPT_FILTER_GRP.md) | `RPT_FILTER_GRP_ID` |
| `RPT_PREFS_REF_ID` | [SN_RPT_PREFS_REF](SN_RPT_PREFS_REF.md) | `RPT_PREFS_REF_ID` |

