# PRACTICE_SITE_MSG_ROUTING

> Routing rules are used to create intended recipients and routed recipients for secure messages from the consumer.

**Description:** PRACTICE SITE MSG ROUTING RULE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `INTENDED_RECIPIENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The intended recipient of the message. This field must be 0 if a non-zero value is used for INTENDED_RECIPIENT_PRSNL_GROUP_ID |
| 6 | `INTENDED_RECIP_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | PERSONNEL GROUP ID |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `MESSAGE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of message for which this routing rule applies |
| 9 | `PRACTICE_SITE_ID` | DOUBLE | NOT NULL | FK→ | The practice site for which this routing rule applies |
| 10 | `PRACTICE_SITE_MSG_ROUTING_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `ROUTED_RECIPIENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The routed recipient of the message. May be 0. This field must be 0 if a non-zero value is used for ROUTED_RECIPIENT_PRSNL_GROUP_ID |
| 12 | `ROUTED_RECIP_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | PERSONNEL GROUP ID |
| 13 | `ROUTING_RULE_TYPE` | VARCHAR(28) |  |  | This is used to determine different types of routing rules |
| 14 | `SUPPLEMENTAL_DISPLAY` | VARCHAR(100) |  |  | This will be appended as a suffix to the name of the intended recipient |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTENDED_RECIPIENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `INTENDED_RECIP_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PRACTICE_SITE_ID` | [PRACTICE_SITE](PRACTICE_SITE.md) | `PRACTICE_SITE_ID` |
| `ROUTED_RECIPIENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ROUTED_RECIP_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

