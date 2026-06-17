# SI_ESO_TRIG_ROUT_R_HIST

> This table stores all modifications made to the ESO_Trig_Routine_R table.

**Description:** System Integration ESO Trigger Routine Relation HistoryThis table stores all mod  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl ID of the user who made new modification on the Outbound_Field_Processing table |
| 6 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl ID of the user who made original record on the Outbound_Field_Processing table |
| 7 | `PARENT_ACTIVE_IND` | DOUBLE | NOT NULL |  | Parent Active Indicator used to track the active indicator of the Parent Table. |
| 8 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Beg_Eff_Dt_TM from the ESO_TRIG_ROUTINE_R Table |
| 9 | `RELATED_TRIG_ROUT_ARG_ID` | DOUBLE | NOT NULL |  | Related identifier used for recursive relationship within this table. |
| 10 | `ROUTINE_ARGS` | VARCHAR(255) | NOT NULL |  | Routine Argument |
| 11 | `ROUTINE_CONTROL` | DOUBLE | NOT NULL |  | Routine Control Arguments |
| 12 | `ROUTINE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to ESO_Routine |
| 13 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Order of Arguments for the Trigger/Routine combination |
| 14 | `SI_ESO_TRIG_ROUT_R_HIST_ID` | DOUBLE | NOT NULL |  | System Integration Trigger Routine Argument History Identifier - Primary Key |
| 15 | `TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to ESO_Trigger |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ROUTINE_ID` | [ESO_TRIG_ROUTINE_R](ESO_TRIG_ROUTINE_R.md) | `ROUTINE_ID` |
| `TRIGGER_ID` | [ESO_TRIG_ROUTINE_R](ESO_TRIG_ROUTINE_R.md) | `TRIGGER_ID` |

