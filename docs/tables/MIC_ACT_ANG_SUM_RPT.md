# MIC_ACT_ANG_SUM_RPT

> This table contains the content required to generate a summary report for ANG.

**Description:** This tables houses temporary information to create the ANG Summary Report.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANG_RUN_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value which associates this record with a particular run of the auto no growth reporting process. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 4 | `ERROR_TEXT` | VARCHAR(150) |  |  | This field contains the text associated with the error generated from the auto no growth process for this record. |
| 5 | `LOAD_DT_TM` | DATETIME |  |  | This field identifies either the start date and time of the orderable procedure or the initial load date and time of the media. Some blood culture instrument interfaces do not send and initial load date and time to the Cerner system, in which case the start date and time of the procedure is used inthis field. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 7 | `ORDER_LOCK_DT_TM` | DATETIME |  |  | This field identifies the date and time the record was locked. When the user exits the microbiology application accessing the accession this field will be set to null. |
| 8 | `ORDER_LOCK_ID` | DOUBLE | NOT NULL |  | This field identifies the id of the person that currently has this order_id locked. The order_lock_id corresponds to the person_id on the prsnl table, which identifies the user. When the user exits the microbiology application accessing the accession this field will be set to null. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `PRINT_REPORT_FLAG` | DOUBLE | NOT NULL |  | This field indicates the type of error identified for the record. If this field is defined greater than 0, then the error_text field will also be defined. Valid values include: 0 = Successful 1 =Batch reporting process failed 2 = Accession locked 3 = Performed only report 4 = Report exceeds procedure's report limit 5 = Final report already issued, please review results. |
| 11 | `PRINT_SEQ` | DOUBLE | NOT NULL |  | This field identifies the sequence with which this record should be printed on the auto no growth summary report. If a record has already been printed on a summary report this field will be set to 0. When a record is first written to the table this field will be set to 1. As additional runs are created the previous runs print_seq number is incremented such that the records from the oldest run w |
| 12 | `REPORT_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the report task to be issued for this ang_id. Reports are defined on code set 1000, Microbiology Reports. |
| 13 | `REPORT_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the current status of the report. The status code_value is from code set 1901Result Status. |
| 14 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the instrument or bench for which automatic no growth times are defined. |
| 15 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define auto no growth reporting parameters. All three levels of source hierarchy (source, section, category) can be used in defining auto nogrowth reporting parameters. |
| 16 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to the report task associated with the orderable procedure. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANG_RUN_ID` | [MIC_ANG_STATUS](MIC_ANG_STATUS.md) | `ANG_RUN_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REPORT_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

