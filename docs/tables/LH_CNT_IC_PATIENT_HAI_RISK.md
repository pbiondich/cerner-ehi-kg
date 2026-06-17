# LH_CNT_IC_PATIENT_HAI_RISK

> This table stores hospital acquired infection risk information related to patient

**Description:** LH CNT IC PATIENT HAI RISK  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_IC_PATIENT_HAI_RISK_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BSI_IND` | DOUBLE | NOT NULL |  | 0=No BSI risk, 1=BSI risk |
| 3 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Stores date time when the row is created. |
| 4 | `HAI_DISPLAY` | VARCHAR(255) |  |  | Shows which HAI risks the patient has |
| 5 | `LH_CNT_IC_PATIENT_HAI_RISK_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_HAI_RISK table. |
| 6 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to lh_cnt_ic_patient_pop. |
| 7 | `PNEU_IND` | DOUBLE | NOT NULL |  | 0=No PNEU risk, 1=PNEU risk |
| 8 | `SSI_IND` | DOUBLE | NOT NULL |  | 0=No SSI risk, 1=SSI risk |
| 9 | `SURGERY_DT_TM` | DATETIME |  |  | The surgery_dt_tm on the lh_cnt_ic_patient_hai_risk table is the date and time the surgery was completed that triggered the SSI HAI Risk. |
| 10 | `SURGERY_NAME` | VARCHAR(40) |  |  | The surgery_name on the lh_cnt_ic_patient_hai_risk tables is the name of the surgery that triggered the SSI HAI Risk. |
| 11 | `SURG_PROC_CD` | DOUBLE | NOT NULL |  | Stores code value of the surgical procedure order |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `UTI_IND` | DOUBLE | NOT NULL |  | 0=No UTI risk, 1=UTI risk |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_CNT_IC_PAT_HAI_CODE](LH_CNT_IC_PAT_HAI_CODE.md) | `LH_CNT_IC_PATIENT_HAI_RISK_ID` |

