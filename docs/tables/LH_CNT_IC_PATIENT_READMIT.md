# LH_CNT_IC_PATIENT_READMIT

> 0

**Description:** LH CNT IC PATIENT READMIT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to lh_cnt_ic_patient_pop |
| 3 | `LH_CNT_IC_PATIENT_READMIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_READMIT table. |
| 4 | `READMIT_30_IND` | DOUBLE | NOT NULL |  | Indicates whether this patient's encounter occurred with 30 days of being discharged from a previous encounter. 0=no, 1 = yes |
| 5 | `READMIT_30_SURG_DT_TM` | DATETIME |  |  | The date/time the previous surgery occurred |
| 6 | `READMIT_30_SURG_IND` | DOUBLE | NOT NULL |  | Indicates whether this patient's encounter occurred with 30 days of being discharged from a previous surgery encounter. 0=no, 1 = yes |
| 7 | `READMIT_365_IMPLANT_DT_TM` | DATETIME |  |  | The date/time the surgical implant occurred. |
| 8 | `READMIT_365_IMPLANT_IND` | DOUBLE | NOT NULL |  | Indicates whether this patient's encounter occurred with 365 days of being discharged from a previous encounter that had a surgical implant performed. 0=no, 1 = yes |
| 9 | `READMIT_90_SURG_DT_TM` | DATETIME |  |  | The date/time of the surgery that occurred within the previous 90 days of this encounter's registration date/time. |
| 10 | `READMIT_90_SURG_IND` | DOUBLE | NOT NULL |  | Indicates whether this patient's encounter occurred with 90 days of having surgery. 0=no, 1=yes. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |

