# PFT_BR_LINE_STATUS_DETAIL

> Stores the claim line acknowledgements from the payer.

**Description:** ProFit Bill Record Claim Line Status Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDL_STATUS_INFO_TXT` | VARCHAR(1000) |  |  | Stores additional status information. |
| 3 | `CREATED_DT_TM` | DATETIME |  |  | The date and time this row was created. |
| 4 | `PFT_BR_CLAIM_STATUS_DETAIL_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the PFT_BR_CLAIM_STATUS_DETAIL table. |
| 5 | `PFT_BR_LINE_STATUS_DETAIL_ID` | DOUBLE | NOT NULL |  | A system generated number used to uniquely identify a row on the PFT_BR_LINE_STATUS_DETAIL table. |
| 6 | `PFT_LINE_ITEM_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the PFT_LINE_ITEM table. |
| 7 | `SVC_LINE_ENTITY_CD` | DOUBLE |  |  | Stores the entity code for the claim line. |
| 8 | `SVC_LINE_STATUS_CATEGORY_CD` | DOUBLE |  |  | Indicates the general category of a claim line status. |
| 9 | `SVC_LINE_STATUS_CATEGORY_TXT` | VARCHAR(30) |  |  | Indicates the general category in a textual format of a claim line status. |
| 10 | `SVC_LINE_STATUS_CD` | DOUBLE |  |  | This code conveys the staus of a claim line item. |
| 11 | `SVC_LINE_STATUS_DT_TM` | DATETIME |  |  | The date and time of the status codes that were sent in from upstream. |
| 12 | `SVC_LINE_STATUS_TXT` | VARCHAR(30) |  |  | Conveys the status of a claim line item in a textual format. |
| 13 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_BR_CLAIM_STATUS_DETAIL_ID` | [PFT_BR_CLAIM_STATUS_DETAIL](PFT_BR_CLAIM_STATUS_DETAIL.md) | `PFT_BR_CLAIM_STATUS_DETAIL_ID` |
| `PFT_LINE_ITEM_ID` | [PFT_LINE_ITEM](PFT_LINE_ITEM.md) | `PFT_LINE_ITEM_ID` |

