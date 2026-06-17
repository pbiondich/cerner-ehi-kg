# RCA_RULE_SERVICE_PARAM

> This table contains parameters related to RCA rule services.

**Description:** Revenue Cycle Service Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DATA_TYPE_CD` | DOUBLE | NOT NULL |  | The code value of the parameter's data type. Values come from code set 4124000. |
| 3 | `FIELD_KEY_TXT` | VARCHAR(255) | NOT NULL |  | The key that identifies the field that the value comes from, which is being passed into the service as a parameter. |
| 4 | `LITERAL_IND` | DOUBLE | NOT NULL |  | This indicator indicates whether or not the value stored in the FIELD_KEY_TXT is a literal value or not. |
| 5 | `RCA_RULE_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Rule Service that is using this record. |
| 6 | `RCA_RULE_SERVICE_PARAM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RCA_RULE_SERVICE_PARAM table. |
| 7 | `SERVICE_KEY_TXT` | VARCHAR(100) | NOT NULL |  | The key that the service uses to map to the actual field key. We do not want the service to hold the actual field key to support future field key migrations. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCA_RULE_SERVICE_ID` | [RCA_RULE_SERVICE](RCA_RULE_SERVICE.md) | `RCA_RULE_SERVICE_ID` |

