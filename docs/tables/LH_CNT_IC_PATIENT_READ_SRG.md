# LH_CNT_IC_PATIENT_READ_SRG

> Infection Control Worklist table to store surgical procedures that fall within readmission timeframes.

**Description:** LH_CNT_IC_PATIENT_READ_SRG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to LH_CNT_IC_PATIENT_POP table. |
| 3 | `LH_CNT_IC_PATIENT_READ_SRG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_READ_SRG table. |
| 4 | `READMIT_GROUP_FLAG` | DOUBLE | NOT NULL |  | 1=30 day readmit, 2=90 day readmit, 3=365 day readmit after implant |
| 5 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to SURG_CASE_PROCEDURE table. |
| 6 | `SURG_DT_TM` | DATETIME |  |  | Stores the date/time of when the surgical procedure took place. |
| 7 | `SURG_PROC_CD` | DOUBLE | NOT NULL |  | Stores the surgical procedure code from the SURG_CASE_PROCEDURE table. |
| 8 | `SURG_PROC_NHSN_CAT_CD` | DOUBLE | NOT NULL |  | Stores the NHSN code value mapped to a surgical procedure within Bedrock. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

