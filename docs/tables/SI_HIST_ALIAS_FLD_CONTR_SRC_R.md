# SI_HIST_ALIAS_FLD_CONTR_SRC_R

> This table stores historical information for the si_alias_field_contr_src_r_hist table

**Description:** System Integration Alias Field Contributor Source Relation History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_FLD_CONTR_SRC_R_ID` | DOUBLE | NOT NULL | FK→ | Copy of the Alias_field_contr_src_id from the si_alias_field_contr_src_r table |
| 6 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | Copy of the Contributor_source_cd from the si_alias_field_contr_src_r table |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `FIELD_CD` | DOUBLE | NOT NULL |  | Copy of the Field_cd from the si_alias_field_contr_src_r table |
| 9 | `FIELD_NAME` | VARCHAR(256) |  |  | Copy of the Field_name from the si_alias_field_contr_src_r table |
| 10 | `HIST_ALIAS_FLD_CONTR_SRC_R_ID` | DOUBLE | NOT NULL |  | Alias Field Contributor Source Relation History ID |
| 11 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made new modification on the si_alias_field_contr_src_r table |
| 12 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made original modification on the si_alias_field_contr_src_r table |
| 13 | `REC_BEG_EFF_DT_TM` | DATETIME | NOT NULL |  | Copy of the Beg_Eff_Dt_TM from the si_alias_field_contr_src_r table |
| 14 | `SEGMENT_NAME` | VARCHAR(256) |  |  | Copy of the Segment_name from the si_alias_field_contr_src_r table |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_FLD_CONTR_SRC_R_ID` | [SI_ALIAS_FLD_CONTR_SRC_R](SI_ALIAS_FLD_CONTR_SRC_R.md) | `ALIAS_FLD_CONTR_SRC_R_ID` |
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

