# LH_CNT_IC_PATIENT_RPT_RISK

> This table stores patient's RPT risk information

**Description:** LH CNT IC PATIENT RPT RISK  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Stores code value of the body site from where the specimen is collected. |
| 3 | `BODY_SITE_DISPLAY` | VARCHAR(40) |  |  | The body site |
| 4 | `COLLECT_DT_TM` | DATETIME |  |  | The date/time the specimen was collected |
| 5 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Stores date time when the row is created. |
| 6 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code from the clinical event table. |
| 7 | `EVENT_DISPLAY` | VARCHAR(255) |  |  | The display for this reportable event |
| 8 | `EVENT_STATUS_CD` | DOUBLE | NOT NULL |  | Stores the status code of the event. |
| 9 | `EVENT_STATUS_DISPLAY` | VARCHAR(40) |  |  | The event status display |
| 10 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to lh_cnt_ic_patient_pop |
| 11 | `LH_CNT_IC_PATIENT_RPT_RISK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_RPT_RISK table. |
| 12 | `ORDER_DT_TM` | DATETIME |  |  | The date/time the order was placed |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Stores the Id of the associated order. |
| 14 | `ORDER_MNEMONIC` | VARCHAR(100) |  |  | The mnemonic of the order |
| 15 | `ORGANISM_DESCRIPTION` | VARCHAR(2000) |  |  | The description of the organism that caused an infection |
| 16 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | Stores the parent event id from clinical event. |
| 17 | `REPORTABLE_FLAG` | DOUBLE | NOT NULL |  | 1=24HR, 2=OTHER |
| 18 | `RPT_TYPE_FLAG` | DOUBLE | NOT NULL |  | 1=24HR, 2=OTHER |
| 19 | `SOURCE_TYPE_DISPLAY` | VARCHAR(40) |  |  | The source type/site |
| 20 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Stores code value of the type of specimen collected. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

