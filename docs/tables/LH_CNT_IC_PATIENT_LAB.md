# LH_CNT_IC_PATIENT_LAB

> This table stores patient's lab result information.

**Description:** LH CNT IC PATIENT LAB  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Stores code value of the body site from where the specimen is collected. |
| 3 | `BODY_SITE_DISPLAY` | VARCHAR(40) |  |  | The display for the body site |
| 4 | `COLLECTED_DT_TM` | DATETIME |  |  | The date/time the lab specimen was collected |
| 5 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Stores date time when the row is created. |
| 6 | `EVENT_CD` | DOUBLE | NOT NULL |  | Stores the event code from clinical event. |
| 7 | `EVENT_DISPLAY` | VARCHAR(40) |  |  | The display for this lab event |
| 8 | `LAB_TYPE_FLAG` | DOUBLE | NOT NULL |  | Used to determine which type of lab result this is. 1=Micro, 2=Fecal, 3= Sero |
| 9 | `LH_CNT_IC_PATIENT_LAB_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_LAB table. |
| 10 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to lh_cnt_ic_patient_pop |
| 11 | `ORDER_DT_TM` | DATETIME |  |  | The date/time the lab order was placed |
| 12 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order ID of the lab order. |
| 13 | `ORGANISM_DESCRIPTION` | VARCHAR(2000) |  |  | The description of the organism causing infection |
| 14 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | Stores the parent event id from clinical event |
| 15 | `POSITIVE_FLAG` | DOUBLE | NOT NULL |  | Flag to determine if this result is positive, negative, or in progress. 1 = positive, 2 = negative, 3 = in progress |
| 16 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Stores the status code of the result. |
| 17 | `RESULT_STATUS_DISPLAY` | VARCHAR(40) |  |  | The status of the result |
| 18 | `SOURCE_SITE_DISPLAY` | VARCHAR(40) |  |  | The display for the source site |
| 19 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Stores code value of the type of specimen collected |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

