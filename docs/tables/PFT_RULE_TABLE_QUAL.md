# PFT_RULE_TABLE_QUAL

> This table contains qualification information for tables that are built from pft_rule_maint. These tables are uses to query data that pertains to the particular claim that is being generated.

**Description:** ProFit Rule Table Qualification  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONDITIONAL_CD` | DOUBLE | NOT NULL |  | Conditional logic to be applied for the qualification (i.e. AND, OR, etc.) |
| 6 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Priority of each qualification establishing order of sequence. |
| 7 | `QUALIFIER_CD` | DOUBLE | NOT NULL |  | Qualifier predicate to be used in qualification (i.e. =, <, >, etc.) |
| 8 | `QUAL_FIELD_NAME` | VARCHAR(100) | NOT NULL |  | Name of field to be used on left side of qualifier predicate |
| 9 | `QUAL_TABLE_NAME` | VARCHAR(100) | NOT NULL |  | Table to be used on left side of qualifier predicate |
| 10 | `RULE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the information concerning the grouping of qualifications on PFT_RULE_GROUP |
| 11 | `TABLE_QUAL_ID` | DOUBLE | NOT NULL |  | Identifies qualification information for tables built from the pft_rule_maint. Tables are used to query data pertaining to particular claims being generated. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VALUE_DISP` | VARCHAR(100) |  |  | String constant value to be used on right side of qualifier predicate |
| 18 | `VALUE_FIELD_NAME` | VARCHAR(100) |  |  | Name of field to be used on left side of qualifier predicate. |
| 19 | `VALUE_NUMERIC` | DOUBLE |  |  | Numeric constant value to be used on right side of qualifier |
| 20 | `VALUE_TABLE_NAME` | VARCHAR(100) |  |  | Table to be used on left side of qualifier predicate. |
| 21 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | Type of value to be used on right side of qualifier predicate. 1- string value (uses the value_disp field), 2 - numeric value (uses the value_numeric field), 3 - table/field value ( uses the value_tablename and value_fieldname), 4 - date value ( uses the value_disp field) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RULE_GROUP_ID` | [PFT_RULE_GROUP](PFT_RULE_GROUP.md) | `GROUP_ID` |

