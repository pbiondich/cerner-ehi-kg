# LH_CNT_ADVSR_VTE_ACTION

> This table holds VTE scenario information among different guideline types

**Description:** LH_CNT_ADVSR_VTE_ACTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BMI_FLAG` | DOUBLE | NOT NULL |  | This flag determines if the patient's BMI is greater than or equal to 40. 1=Yes; 2=No; 3= NA |
| 2 | `CATEGORY_REQS` | VARCHAR(100) |  |  | Order categories (pharm, mech) that are required for the scenario. |
| 3 | `DELAYED_PHOPHYLAXIS_REASON_TXT` | VARCHAR(100) |  |  | Reason for delayed prophylaxis. |
| 4 | `EST_CRCL_TAG` | VARCHAR(100) |  |  | Calculated value of the creatinine clearance (e.g. <30). |
| 5 | `GUIDELINE_TYPE_NAME` | VARCHAR(30) |  |  | The organization (ACCP, NICE, etc.) that created the guideline |
| 6 | `HIT_CONTRA_ABS_FLAG` | DOUBLE | NOT NULL |  | This flag determines if HIT contraindications have been identified. 1=Yes; 2=No; 3=NA |
| 7 | `LH_CNT_ADVSR_VTE_ACTION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_ADVSR_VTE_ACTION table. |
| 8 | `MECH_CONTRA_IND` | DOUBLE | NOT NULL |  | This flag determines if there a mechanical Contraindication. 1=Yes; 0=No. |
| 9 | `PATIENT_TYPE_TXT` | VARCHAR(100) |  |  | The type of patient identified in the advisor (e.g. Medical or Bariatric Surgery). |
| 10 | `PHARM_CONTRA_ABS_FLAG` | DOUBLE | NOT NULL |  | This flag determines if pharmacologic contraindications have been identified. 1=Yes; 2=No; 3=NA. |
| 11 | `RISK_SCORE_SYSTEM_NAME` | VARCHAR(30) |  |  | The scoring system (caprini, padua, etc.) that is used to assess risk for the patient type. |
| 12 | `RISK_SCORE_TAG` | VARCHAR(100) |  |  | Calculated value of risk score (e.g. >4 Padua) |
| 13 | `SCENARIO_NBR` | DOUBLE | NOT NULL |  | The scenario number that the row describes. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `WEIGHT_ENOXAPARIN_FLAG` | DOUBLE | NOT NULL |  | This flag determines if the patient is on enoxaparin and their weight is less than 45 kg. 1=Yes; 2=No; 3=NA |
| 20 | `WEIGHT_FONDAPARINUX_FLAG` | DOUBLE | NOT NULL |  | This flag determines if the patient is on fondaparinux and their weight is less than 50 kg. 1=Yes; 2=No; 3=NA. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

