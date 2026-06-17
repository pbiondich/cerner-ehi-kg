# RCR_GSR_CONTEXT

> Holds a GSR context with reference to logical domain and time zone.

**Description:** Revenue Cycle Reporting - Gold Standard Reporting Context  
**Table type:** ACTIVITY  
**Primary key:** `RCR_GSR_CONTEXT_ID`  
**Columns:** 9  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 3 | `RCR_GSR_CONTEXT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RCR_GSR_CONTEXT table. |
| 4 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone in which the GSR job is running. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [RCR_GSR_CONTEXT_RELTN](RCR_GSR_CONTEXT_RELTN.md) | `RCR_GSR_CONTEXT_ID` |
| [RCR_GSR_LOCK_INFO](RCR_GSR_LOCK_INFO.md) | `RCR_GSR_CONTEXT_ID` |
| [RC_CLN_AREA](RC_CLN_AREA.md) | `RCR_GSR_CONTEXT_ID` |
| [RC_GSR_DIMENSION_TMP](RC_GSR_DIMENSION_TMP.md) | `RCR_GSR_CONTEXT_ID` |
| [RC_GSR_SUM_AGG_TMP](RC_GSR_SUM_AGG_TMP.md) | `RCR_GSR_CONTEXT_ID` |

