# MM_CNTRCT_HDR_TIER

> Contract Header Tier

**Description:** Contract Header Tier  
**Table type:** REFERENCE  
**Primary key:** `PRICE_TIER_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS_NODE_ID` | DOUBLE | NOT NULL |  | Class Node ID value. |
| 2 | `CNTRCT_ID` | DOUBLE | NOT NULL | FK→ | Contract number key |
| 3 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted |
| 5 | `CREATE_ID` | DOUBLE | NOT NULL |  | User id of person which created this row |
| 6 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row. |
| 7 | `METRIC_CD` | DOUBLE | NOT NULL |  | metric code |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Header price tier organization key |
| 9 | `PRICE_TIER_ID` | DOUBLE | NOT NULL | PK | key to mm_cntrc_hdr_tier |
| 10 | `PRODUCT_LEVEL` | DOUBLE |  |  | Header price tier product level |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNTRCT_ID` | [MM_CNTRCT_HDR](MM_CNTRCT_HDR.md) | `CNTRCT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MM_CNTRCT_LINE_TIER](MM_CNTRCT_LINE_TIER.md) | `HDR_PRICE_TIER_ID` |
| [MM_XFI_CNTRCT_HDR_TIER](MM_XFI_CNTRCT_HDR_TIER.md) | `PRICE_TIER_ID` |

