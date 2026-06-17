# LH_CNT_IC_PAT_HAI_CODE

> This table will contain a list of code values corresponding to each entry in LH_CNT_IC_PATIENT_HAI_RISK.

**Description:** Lighthouse Content Infection Control Patient Hospital Acquired Infection Codes  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HAI_CD` | DOUBLE | NOT NULL |  | Code value of the status of the Infection. |
| 2 | `HAI_EVENT_DT_TM` | DATETIME |  |  | Event Date time corresponding to the HAI event. |
| 3 | `HAI_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the type of HAI (1 : BSI; 2 : PNEU; 4: SSI; 8: UTI) |
| 4 | `LH_CNT_IC_PATIENT_HAI_RISK_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the row on the LH_CNT_IC_PATIENT_HAI_RISK table that is related to the Hospital Aquired Infection Code. |
| 5 | `LH_CNT_IC_PAT_HAI_CODE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PAT_HAI_CODES table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_HAI_RISK_ID` | [LH_CNT_IC_PATIENT_HAI_RISK](LH_CNT_IC_PATIENT_HAI_RISK.md) | `LH_CNT_IC_PATIENT_HAI_RISK_ID` |

