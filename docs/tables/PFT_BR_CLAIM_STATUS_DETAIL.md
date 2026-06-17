# PFT_BR_CLAIM_STATUS_DETAIL

> Stores the claim acknowledgments from the payer.

**Description:** ProFit Bill Record Claim Status Detail  
**Table type:** ACTIVITY  
**Primary key:** `PFT_BR_CLAIM_STATUS_DETAIL_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDL_STATUS_INFO_TEXT` | VARCHAR(1000) |  |  | Stores the additional status information. |
| 3 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | FK→ | Version number of a bill record. |
| 4 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to BILL_REC table. |
| 5 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row is created. |
| 6 | `PAYER_CATEGORY_CD` | DOUBLE | NOT NULL |  | Indicates the general category of a claim's status. |
| 7 | `PAYER_CATEGORY_TXT` | VARCHAR(30) |  |  | Stores the X12 value of the general category of a claim's status. |
| 8 | `PAYER_CONTROL_IDENT` | VARCHAR(50) |  |  | Stores the payer claim control number. |
| 9 | `PAYER_ENTITY_CD` | DOUBLE |  |  | Stores the entity codes. |
| 10 | `PAYER_STATUS_CD` | DOUBLE | NOT NULL |  | These convey the status of an entire claim. |
| 11 | `PAYER_STATUS_DT_TM` | DATETIME |  |  | The date/time of the status codes that sent in from upstream. |
| 12 | `PAYER_STATUS_TXT` | VARCHAR(30) |  |  | Stores the X12 value of the status of an entire claim. |
| 13 | `PFT_BR_CLAIM_STATUS_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique system generated number that identifies a row on the PFT_BR_CLAIM_STATUS_DETAIL table. |
| 14 | `TRANSACTION_CONTROL_IDENT` | VARCHAR(50) | NOT NULL |  | Stores the claim status transaction trace number which is unique for each transaction. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_BR_LINE_STATUS_DETAIL](PFT_BR_LINE_STATUS_DETAIL.md) | `PFT_BR_CLAIM_STATUS_DETAIL_ID` |

