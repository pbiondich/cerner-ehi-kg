# SEC_RES_OPERATIONS

> This table will hold the operations that can be performed on the resources from the sec_resource table. The data for this table will be shipped and is not modifiable at the client site

**Description:** Security Resource Operations  
**Table type:** REFERENCE  
**Primary key:** `SEC_RES_OPERATIONS_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_CONTROL_CHECK_BIT` | DOUBLE | NOT NULL |  | Bit map of binary data representing the checks required for the resource operation (For example, a CDAC check is 1, anLR check is 2, etc.) |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `AUDIT_ADAPTER_TEXT` | VARCHAR(255) | NOT NULL |  | The audit adapter class that will be applied to the operation resource for assembling the audit event participants. This will be the fully qualified name of the java class implementing the audit adapter. |
| 7 | `OPER_NAME` | VARCHAR(50) | NOT NULL |  | The name of the operation. |
| 8 | `RULE_TEXT` | VARCHAR(255) | NOT NULL |  | The rule class that will be applied to the operation resource. This will be the fully qualified name of the java class implementing the rule. |
| 9 | `SEC_POLICY_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the security policy associated with this res operation. |
| 10 | `SEC_RESOURCE_ID` | DOUBLE | NOT NULL | FK→ | The resource that defines the resource operation |
| 11 | `SEC_RES_OPERATIONS_ID` | DOUBLE | NOT NULL | PK | The primary key identifying the resource operation |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEC_POLICY_ID` | [SEC_POLICY](SEC_POLICY.md) | `SEC_POLICY_ID` |
| `SEC_RESOURCE_ID` | [SEC_RESOURCE](SEC_RESOURCE.md) | `SEC_RESOURCE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SEC_RES_OPER_PRIN_R](SEC_RES_OPER_PRIN_R.md) | `SEC_RES_OPERATIONS_ID` |

