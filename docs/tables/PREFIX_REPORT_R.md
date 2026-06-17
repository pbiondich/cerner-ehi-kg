# PREFIX_REPORT_R

> This reference table contains the associations between report order catalog items and case prefixes. This table also includes parameters defining whether or not the report can be ordered multiple times, primary report designation, and display sequence.

**Description:** Prefix Report Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the report order catalog item. This value could be used to join to information stored in the order catalog table. |
| 2 | `DFLT_DIAGNOSTIC_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code representing the report component procedure (discrete task assay) that should default in the code assignment and code review dialogs. |
| 3 | `MULT_ALLOWED_IND` | DOUBLE |  |  | This field contains an indicator documenting whether or not the report can be ordered more than one time for a single case. Final reports, for example, should not be ordered more than one time, while multiple orders for an addendum reports may be valid. |
| 4 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to represent the accession prefix value to which reports are associated on the PREFIX_REPORT_R table. |
| 5 | `PRIMARY_IND` | DOUBLE |  |  | This field contains an indicator documenting whether or not the report represents the primary report for a case. The primary report is the report that is always associated with every case assigned the prefix value included in the key to this table. |
| 6 | `REPORTING_SEQUENCE` | DOUBLE |  |  | This field contains a value which determines the report's hierarchical sequence (when compared to other reports) used for report presentation. This field is used when multiple reports are present for the same pathology case. |
| 7 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL |  | The report type to which the prefix report relates. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `DFLT_DIAGNOSTIC_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |

