# SN_CHARGE_DETAIL

> SurgiNet Charge Detail Table

**Description:** SurgiNet Charge Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CEA_TYPE_CD` | DOUBLE | NOT NULL |  | The charge event activity type associated with the transaction. |
| 2 | `CHARGE_DETAIL_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a charge detail. |
| 3 | `CHARGE_HEADER_ID` | DOUBLE | NOT NULL | FK→ | The charge header associated with this charge detail. |
| 4 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | The charge type associated with the transaction. |
| 5 | `EXT_ITEM_EVENT_ID` | DOUBLE | NOT NULL |  | External Item Event ID. |
| 6 | `EXT_ITEM_EVENT_NAME` | VARCHAR(32) |  |  | Contains the table name which primary key is stored in ext_item_event_id field. |
| 7 | `EXT_ITEM_REFERENCE_ID` | DOUBLE | NOT NULL |  | External Item Reference ID. |
| 8 | `EXT_ITEM_REFERENCE_NAME` | VARCHAR(32) |  |  | Contains the table name which primary key is stored in ext_item_reference_id field. |
| 9 | `EXT_MASTER_EVENT_ID` | DOUBLE | NOT NULL |  | External Master Event ID. |
| 10 | `EXT_MASTER_EVENT_NAME` | VARCHAR(32) |  |  | Contains the table name which primary key is stored in ext_master_event_id field. |
| 11 | `EXT_PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | External Parent Event ID. |
| 12 | `EXT_PARENT_EVENT_NAME` | VARCHAR(32) |  |  | Contains the table name which primary key is stored in ext_parent_event_id field. |
| 13 | `EXT_PARENT_REFERENCE_ID` | DOUBLE | NOT NULL |  | External Parent Reference ID. |
| 14 | `EXT_PARENT_REFERENCE_NAME` | VARCHAR(32) |  |  | Contains the table name which primary key is stored in ext_parent_reference_id field. |
| 15 | `QTY` | DOUBLE | NOT NULL |  | The quantity of the transaction. |
| 16 | `RECHARGED_IND` | DOUBLE | NOT NULL |  | Indicates the recharged status of the transaction (0 = False, 1 = True). |
| 17 | `RECHARGE_DT_TM` | DATETIME |  |  | The date and time the transaction was recharged. |
| 18 | `RECHARGE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who requested to recharge the transaction. |
| 19 | `RESULT` | DOUBLE | NOT NULL |  | The result value of the transaction. |
| 20 | `ROOT_DETAIL_ID` | DOUBLE | NOT NULL |  | The parent ID of the transaction. |
| 21 | `TOTAL_CHARGED_QTY` | DOUBLE | NOT NULL |  | Total charged quantity. |
| 22 | `TOTAL_CHARGED_RESULT` | DOUBLE | NOT NULL |  | Total charged result value. |
| 23 | `TRANS_DESC` | VARCHAR(250) |  |  | Description of the transaction. |
| 24 | `TRANS_DT_TM` | DATETIME |  |  | The date and time of the transaction. |
| 25 | `TRANS_TYPE_MEAN` | VARCHAR(12) |  |  | The type of transaction. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_HEADER_ID` | [SN_CHARGE_HEADER](SN_CHARGE_HEADER.md) | `CHARGE_HEADER_ID` |
| `RECHARGE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

