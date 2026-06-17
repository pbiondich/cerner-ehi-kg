# SERVICE_TYPE_GROUPING

> Represents the groupings of encounter type codes or appointment type codes to service type codes for Insurance Eligibility transactions.

**Description:** Service Type Grouping  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The logical domain id for which the grouping applies. |
| 2 | `PARENT_CD` | DOUBLE | NOT NULL |  | The encounter type code value or appointment type code value that is related to the service type. Must be a value from code set 71 or 14230. |
| 3 | `PARENT_CODE_SET` | DOUBLE | NOT NULL |  | The code set of the parent_cd. Either 71 or 14230. |
| 4 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority of the service_type_grouping row for a given parent_cd and logical_domain_id. |
| 5 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The requested eligibility service type . |
| 6 | `SERVICE_TYPE_GROUPING_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

