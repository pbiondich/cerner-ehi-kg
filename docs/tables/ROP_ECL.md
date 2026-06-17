# ROP_ECL

> MDI rules for encounter selection.

**Description:** ROP ECL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CODE_SET` | DOUBLE | NOT NULL |  | The codeset to which the "qual_value" applies to. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date/Time the record was createdColumn |
| 4 | `DEFAULT_OPERATOR_ID` | DOUBLE | NOT NULL | FK→ | The operator id that will be passed to PathNet when the device fails to send an operator id or the operator id sent does not match one on the prsnl_alias table. |
| 5 | `PRSNL_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | The personnel alias pool code used to translate operator ids for this ROP service resource. |
| 6 | `PRSNL_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | The personnel alias type code used to translate operator ids for this ROP service resource. |
| 7 | `QUAL_VALUE` | DOUBLE | NOT NULL |  | Code Value of the qualifier to which the rule it built against. |
| 8 | `ROP_CONFIG_BIT` | DOUBLE |  |  | A bit mapped variable where each bit represents a ROP function. If the bit is 0 the functionality is off, if the bit is 1 the functionality is on. |
| 9 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | POC service resource to which a specific rule applies |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFAULT_OPERATOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

