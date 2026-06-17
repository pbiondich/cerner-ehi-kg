# MM_XFI_REQ_FILL_LOT

> Interface staging table to store the lot information associated to a fill interface transaction. Data is moved from this table to LOT_NUMBER_INFO and LOT_NUMBER_LOCATION_INFO.

**Description:** Interface Requisition Fill Lot  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_EXP_DT_TM` | DATETIME |  |  | Expiration Date as determined at place of origin. |
| 2 | `ABS_EXP_TZ` | DOUBLE |  |  | Time zone associated with the ABS_EXP_DT_TM column. |
| 3 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Used to determine if the system should create lots that don't already exist. |
| 4 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code Value |
| 5 | `EXP_DT_TM` | DATETIME |  |  | The date/time the lot expires. |
| 6 | `INCREASE_IND` | DOUBLE | NOT NULL |  | Used to determine if the lot quantity is an increase or decrease. 0 = decrease, 1 = increase |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `LOT_NUMBER` | VARCHAR(40) | NOT NULL |  | A string value that will be used to resolve against a lot number in Millennium |
| 9 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Associated lot number information |
| 10 | `LOT_QTY` | DOUBLE | NOT NULL |  | Number of items in the lot. |
| 11 | `MFR_CD` | DOUBLE | NOT NULL |  | Codified value of the resolved manufacturer. |
| 12 | `MFR_DT_TM` | DATETIME |  |  | Date/time the lot was manufactured. |
| 13 | `MFR_TXT` | VARCHAR(60) | NOT NULL |  | A string value that will be resolved to a manufacturer in Millennium. |
| 14 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | Defines the state of the row in the upload process. |
| 15 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary key to the table. |
| 16 | `TRANS_HEADER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the MM_XFI_REQ_FILL table. Used to link the parent record on MM_XFI_REQ_FILL to the child lots. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `TRANS_HEADER_ID` | [MM_XFI_REQ_FILL](MM_XFI_REQ_FILL.md) | `TRANSACTION_ID` |

