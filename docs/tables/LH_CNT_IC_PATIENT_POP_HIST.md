# LH_CNT_IC_PATIENT_POP_HIST

> Infection Control Worklist history table for patient movement between categories.

**Description:** LH_CNT_IC_PATIENT_POP_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEVICE_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a device is what triggered a patient onto the ICP Worklist. |
| 3 | `FECAL_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a fecal is what triggered a patient onto the ICP Worklist. |
| 4 | `ISOLATION_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that an isolation is what triggered a patient onto the ICP Worklist. |
| 5 | `LH_CNT_IC_PATIENT_POP_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_POP_HIST table. |
| 6 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to LH_CNT_IC_PATIENT_POP table. |
| 7 | `MICRO_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a micro is what triggered a patient onto the ICP Worklist. |
| 8 | `NOTIF_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a notification is what triggered a patient onto the ICP Worklist. |
| 9 | `PATIENT_GROUP_DT_TM` | DATETIME |  |  | Stores the date and time that a patient's PATIENT_GROUP_FLAG was updated. |
| 10 | `PATIENT_GROUP_FLAG` | DOUBLE | NOT NULL |  | Currently stores a value of 0 - 3 which corresponds to a particular grouping such as Needs Assessment, Ongoing Assessment, Deleted etc. |
| 11 | `PATIENT_INFO_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a change in patient information is what triggered a patient onto the ICP Worklist. |
| 12 | `RISK_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a risk is what triggered a patient onto the ICP Worklist. |
| 13 | `SERO_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a sero is what triggered a patient onto the ICP Worklist. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `XRAY_TRIGGER_IND` | DOUBLE | NOT NULL |  | Stores a 0 or 1 indicating that a xray is what triggered a patient onto the ICP Worklist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |

