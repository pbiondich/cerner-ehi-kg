# SI_ALIAS_FLD_CONTR_SRC_R

> This table contains relations between alias fields and contributor sources.

**Description:** System Integration Alias Field Contributor Source Relation  
**Table type:** REFERENCE  
**Primary key:** `ALIAS_FLD_CONTR_SRC_R_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_FLD_CONTR_SRC_R_ID` | DOUBLE | NOT NULL | PK | Alias Field Contributor Source Identifier. Primary Key. |
| 6 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | The contributor source that should be used for the alias field |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. Contributor System Code |
| 8 | `FIELD_CD` | DOUBLE | NOT NULL |  | The alias field that should use the special coding system |
| 9 | `FIELD_NAME` | VARCHAR(256) |  |  | Name of the segment in which the alias field is located |
| 10 | `SEGMENT_NAME` | VARCHAR(256) |  |  | Name of the segment in which the alias field is located |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_HIST_ALIAS_FLD_CONTR_SRC_R](SI_HIST_ALIAS_FLD_CONTR_SRC_R.md) | `ALIAS_FLD_CONTR_SRC_R_ID` |

