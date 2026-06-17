# ORM_ERX_ACTIVITY_LOG

> This table stores the formulary status viewing history for RxHub reporting purpose.

**Description:** Order Management ePrescribing Activity Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FB_AGE_LIMIT_IND` | DOUBLE |  |  | Indicates if the age limit detail was displayed. |
| 3 | `FB_BENEFIT_SET_ID` | DOUBLE | NOT NULL |  | **OBSOLETE COLUMN**Formulary set id associated to the patient. It is the primary key of table FB_BENEFIT_SET. |
| 4 | `FB_BENEFIT_SET_UID_TXT` | VARCHAR(255) | NOT NULL |  | The formulary benefit set unique id associated to the patient. |
| 5 | `FB_COPAY_FIXED_AMT` | DOUBLE |  |  | Patient cost as a flat dollar amount (No $ sign, USD). |
| 6 | `FB_COPAY_MTHD_TXT` | VARCHAR(20) |  |  | Copay type to consider first (Flat, Percent) if both provided. |
| 7 | `FB_COPAY_PCT_NBR` | DOUBLE |  |  | Percent of the total drug price patient is responsible to pay (0.0 - 1.0). |
| 8 | `FB_COPAY_TIER_NBR` | DOUBLE |  |  | The drug's tier as an indication of cost to the patient. Higher tiers denote lower cost. |
| 9 | `FB_DETAIL_VIEWED_IND` | DOUBLE | NOT NULL |  | Indicates whether formulary detail dialog was shown to the user. |
| 10 | `FB_FORMULARY_STATUS` | DOUBLE |  |  | Formulary status, the relative value and effectiveness of the drug. |
| 11 | `FB_GENDER_LIMIT_IND` | DOUBLE |  |  | Indicates if the age limit detail was displayed. |
| 12 | `FB_MED_NECESSITY_IND` | DOUBLE |  |  | Indicates if the medical necessity detail was displayed. |
| 13 | `FB_PRIOR_AUTH_IND` | DOUBLE |  |  | Indicates if the prior authorization detail was displayed. |
| 14 | `FB_PROD_EXC_IND` | DOUBLE |  |  | Indicates if the drug exclusion detail was displayed. |
| 15 | `FB_QTY_LIMIT_IND` | DOUBLE |  |  | Indicates if the quantity limit detail was displayed. |
| 16 | `FB_RSRC_DRUG_IND` | DOUBLE |  |  | Indicates if the specific resource link detail was displayed. |
| 17 | `FB_RSRC_SMRY_IND` | DOUBLE |  |  | Indicates if the summary level resource link detail was displayed. |
| 18 | `FB_STEP_MEDS_IND` | DOUBLE |  |  | Indicates if the step medication detail was displayed. |
| 19 | `FB_STEP_THERAPY_IND` | DOUBLE |  |  | Indicates if the step therapy detail was displayed. |
| 20 | `FB_TXT_MSG_IND` | DOUBLE |  |  | Indicates if the text message detail was displayed. |
| 21 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order id of the prescription. |
| 22 | `ORM_ERX_ACTIVITY_LOG_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is internally generated. |
| 23 | `REQ_ROUTING_TYPE_FLAG` | DOUBLE | NOT NULL |  | Routing method used for the prescription. 0 - Unknown routing type, 1 - Do not route, 2 - Route to printer, 3 - Route to pharmacy, 4 - Route to fax. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

