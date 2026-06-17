# MM_XFI_CNTRCT_HDR_TIER

> Table used to store relationships between contracts and header price tiers. Data is moved from this table to MM_CNTRCT_HDR_TIER.

**Description:** MM XFI CNTRCT HDR TIER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Header price tier action flag |
| 2 | `CLASS_NODE` | VARCHAR(60) |  |  | Header price tier class node |
| 3 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Class Node ID value. |
| 4 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 5 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 9 | `ORGANIZATION` | VARCHAR(100) |  |  | Header price tier organization |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Header price tier organization key |
| 11 | `PRICE_TIER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to mm_cntrc_hdr_tier |
| 12 | `PROCESS_FLAG` | DOUBLE |  |  | process flag |
| 13 | `PRODUCT_LEVEL` | DOUBLE |  |  | Header price tier product level |
| 14 | `TIER_METRIC` | VARCHAR(60) |  |  | Header price tier metric |
| 15 | `TIER_METRIC_CD` | DOUBLE | NOT NULL |  | Header price tier metric code value |
| 16 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary key |
| 17 | `TRANS_PARENT_ID` | DOUBLE | NOT NULL | FK→ | transaction parent identifier |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRICE_TIER_ID` | [MM_CNTRCT_HDR_TIER](MM_CNTRCT_HDR_TIER.md) | `PRICE_TIER_ID` |
| `TRANS_PARENT_ID` | [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `TRANSACTION_ID` |

