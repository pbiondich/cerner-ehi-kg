# FSI_CLOUD_ESO_ROUTE_INFO

> Maintains the type information of the transactions that will be routed to FSI Cloud/FSI 2.0 ;

**Description:** Foreign System Interfaces Cloud External Systems Outbound Routing Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLASS_TXT` | VARCHAR(15) |  |  | ESO server processing class for which the routing rule applies to. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | Date and time of creation of the routing rule. |
| 4 | `FSI_CLOUD_ESO_ROUTE_INFO_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 6 | `ROUTING_INFO_IDENT` | VARCHAR(36) |  |  | Unique identifier of the source routing rule in OCI database. |
| 7 | `SUBTYPE_TXT` | VARCHAR(15) |  |  | ESO server processing subtype for which the routing rule applies to. |
| 8 | `TYPE_TXT` | VARCHAR(15) |  |  | ESO server processing type for which the routing rule applies to. |
| 9 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

