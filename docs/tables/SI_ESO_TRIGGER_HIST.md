# SI_ESO_TRIGGER_HIST

> This table stores all modifications made to the ESO_Trigger table.

**Description:** System Integration ESO Trigger History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CALL_SRV_FLAG` | DOUBLE | NOT NULL |  | Defines interaction with the ESO Servers |
| 6 | `DESCRIPTION` | VARCHAR(30) | NOT NULL |  | This string provides a description of the event trigger row. |
| 7 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl ID of the user who made new modification on the Outbound_Field_Processing table |
| 8 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl ID of the user who made original record on the Outbound_Field_Processing table |
| 9 | `PARENT_ACTIVE_IND` | DOUBLE | NOT NULL |  | Parent Active Indicator used to track the active indicator of the Parent Table. |
| 10 | `PROCESSING_CONTROL` | DOUBLE | NOT NULL |  | Processing Control number |
| 11 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Beg_Eff_Dt_TM from the ESO_TRIGGER Table |
| 12 | `SERVER_PRCS_CLASS` | VARCHAR(30) | NOT NULL |  | Identifies the ESO server processing class of the transaction. |
| 13 | `SERVER_PRCS_SUBTYPE` | VARCHAR(30) | NOT NULL |  | Identifies the ESO server processing subtype of the transaction. |
| 14 | `SERVER_PRCS_TYPE` | VARCHAR(30) | NOT NULL |  | Identifies the ESO server processing type of the transaction. |
| 15 | `SI_ESO_TRIGGER_HIST_ID` | DOUBLE | NOT NULL |  | System Integration ESO Trigger History ID - Primary Key |
| 16 | `TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to ESO_Trigger table |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRIGGER_ID` | [ESO_TRIGGER](ESO_TRIGGER.md) | `TRIGGER_ID` |

