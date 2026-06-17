# EKS_MODULE_AUDIT_DET

> As modules are logged to the audit table (eks_module_audit), this table is updated with information pertaining to each template used in the logic and actions sections. And one row is created for each in the table.

**Description:** module audit template details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL |  | Accession id associated with the template at runtime |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 3 | `LOGGING` | VARCHAR(2000) |  |  | Text logging information field used by the template to log messages. |
| 4 | `MODULE_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | Relates to the module audit header record. This record is a detail record created to relate a specific template's detail info when a module runs. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL |  | If an order is associated with the template at runtime, it's order Id will be contained in this field. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task assay code (if applicable) associated with the current Expert template |
| 8 | `TEMPLATE_ALIAS` | VARCHAR(50) |  |  | The template alias name defined for a Discern rule/template instance. |
| 9 | `TEMPLATE_NAME` | CHAR(30) |  |  | Template executed for the current audit record |
| 10 | `TEMPLATE_NUMBER` | DOUBLE | NOT NULL |  | ordinal number of the template within the module that fired. |
| 11 | `TEMPLATE_RETURN` | DOUBLE |  |  | return value from the template ( 0 - 100 ) |
| 12 | `TEMPLATE_TYPE` | CHAR(1) |  |  | Template type E)voke, L)ogic, A)ction. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MODULE_AUDIT_ID` | [EKS_MODULE_AUDIT](EKS_MODULE_AUDIT.md) | `REC_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

