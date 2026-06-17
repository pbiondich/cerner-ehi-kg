# ORDER_ALIAS

> This table holds aliases to an order within the system.

**Description:** This table holds alias numbers to an order within the systems.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(200) |  |  | The alias is an identifier for an order. The alias may be unique or non-unique depending on the type of alias. |
| 6 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | The alias pool code identifies a unique set or list of order identifiers. |
| 7 | `ASSIGN_AUTHORITY_SYS_CD` | DOUBLE | NOT NULL |  | This field determines whether the ESI Server received an order alias that was configured for Hold. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BILL_ORD_NBR_IND` | DOUBLE |  |  | Identifies the alias that can be sent with outbound charges. |
| 10 | `CHECK_DIGIT` | DOUBLE |  |  | The check digit of the alias. |
| 11 | `CHECK_DIGIT_METHOD_CD` | DOUBLE | NOT NULL |  | the check digit method code identifies a specific routine, using the alias field, to calculate a check digit. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 14 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `ORDER_ALIAS_ID` | DOUBLE | NOT NULL |  | The id for this order alias. The primary key of the table. |
| 17 | `ORDER_ALIAS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The order alias subtype code further defines the type of alias. |
| 18 | `ORDER_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | The order alias type code identifies a kind or type of alias. |
| 19 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The id of the order. |
| 20 | `PRIMARY_DISPLAY_IND` | DOUBLE |  |  | Indicator for Primary Display |
| 21 | `SYSTEM_TXT` | VARCHAR(4000) |  |  | The system text identifies the external system the order alias belongs to. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `VERSION_TXT` | VARCHAR(4000) |  |  | The version text identifies the version of the alias in the external system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

