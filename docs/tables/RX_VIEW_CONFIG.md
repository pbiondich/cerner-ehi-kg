# RX_VIEW_CONFIG

> Configuration of various views corresponding to users individually and in a group(system level views).

**Description:** Pharmacy View Configuration  
**Table type:** REFERENCE  
**Primary key:** `RX_VIEW_CONFIG_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIG_TYPE_CD` | DOUBLE | NOT NULL |  | Code value representing the Configuration type. |
| 2 | `CONSULT_FUTURE_ORDER_HRS` | DOUBLE |  |  | Indicates the number of hours until start for which future consult orders will be displayed. |
| 3 | `CONSULT_FUTURE_ORDER_IND` | DOUBLE |  |  | Indicates if future consult orders should be displayed. |
| 4 | `CONSULT_FUTURE_ORDER_ONLY_IND` | DOUBLE |  |  | Indicates if only future consult orders should be displayed. |
| 5 | `DISCHARGE_DAYS` | DOUBLE | NOT NULL |  | Number of discharge days to retrieve |
| 6 | `DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | The display name of the configuration. |
| 7 | `FUTURE_ORDER_HRS` | DOUBLE | NOT NULL |  | Indicates the number of hours until start for which future orders will be displayed. |
| 8 | `FUTURE_ORDER_IND` | DOUBLE | NOT NULL |  | Indicates if future orders should be displayed. |
| 9 | `FUTURE_ORDER_ONLY_IND` | DOUBLE |  |  | Indicates if only future orders should be displayed. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `MED_RECONCILIATION_FLAG` | DOUBLE | NOT NULL |  | Differentiates between pharmacy review or supply review or both. |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | ID of the person to whom this view belongs to. Zero if a system-level view. |
| 13 | `RX_VIEW_CONFIG_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_VIEW_CONFIG table. |
| 14 | `SCHEDULED_ORDER_FLAG` | DOUBLE | NOT NULL |  | Indicates values for filtering the orders based on whether they are scheduled or Non Scheduled or include all orders." |
| 15 | `SPLIT_VERIFICATION_FLAG` | DOUBLE | NOT NULL |  | Differentiates between product assign or clinical assign or both. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `VERIFICATION_PROGRESS_FLAG` | DOUBLE |  |  | Allows the user to specify how they would like multiple verification orders to be displayed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_VIEW_CONFIG_DETAIL](RX_VIEW_CONFIG_DETAIL.md) | `RX_VIEW_CONFIG_ID` |

