# DCP_PL_QUERY_TEMP_ACCESS

> Defines which users or groups of users (User Group) have access to utilize a query template.

**Description:** DCP PL QUERY TEMP ACCESS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position that is to be granted access to the specified template. |
| 2 | `PROVIDER_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The id of the provider group that is to be granted access to the specified template. |
| 3 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Provider IdentifierColumn |
| 4 | `TEMPLATE_ACCESS_ID` | DOUBLE | NOT NULL |  | Unique identifier for access definition. |
| 5 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The id of the template that the specified user\position\or group is to be granted access to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROVIDER_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TEMPLATE_ID` | [DCP_PL_QUERY_TEMPLATE](DCP_PL_QUERY_TEMPLATE.md) | `TEMPLATE_ID` |

