# MIC_ANG_AUTOMATED

> This table contains information for each procedure for which auto no growth reporting processing should be applied.

**Description:** Activity tbl, if a record is put on here then that means a report will be order  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANG_ID` | DOUBLE | NOT NULL | FK→ | Hooks back to the specific ang reference record. |
| 2 | `ANG_NEG_SEQ` | DOUBLE | NOT NULL | FK→ | Foreign key from mic_ref_ang_report |
| 3 | `ANG_RUN_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value which associates this record with a particular run of the auto no growth reporting process. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 5 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | whether or not the report will make the order complete |
| 6 | `END_REPORT_RANGE` | DOUBLE | NOT NULL |  | This field identifies the ending time value for the ang report defined. If the first report was issued after 24 hours this field would be set to 24. |
| 7 | `INSTR_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the instrument or bench for which automatic no growth times are defined. |
| 8 | `LAST_PRINT_DT_TM` | DATETIME |  |  | Date/Time that this culture was printed on a summary report. |
| 9 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 10 | `POSITIVE_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the procedure is considered positive. Microbiology procedures are considered positive when a preliminary or final report is issued that includes a positive response or organism. Valid values include: 0 = Not positive 1 = Positive |
| 11 | `PRINT_RPT_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not this report procedure should be printed on an auto no growth summary report. Valid values include: 0 = Do not print 1 = Print on the summary report |
| 12 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the instrument or bench for which automatic no growth times are defined. |
| 13 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define auto no growth reporting parameters. All three levels of source hierarchy (source, section, category) can be used in defining auto nogrowth reporting parameters. |
| 14 | `START_DT_TM` | DATETIME | NOT NULL |  | This field identifies the start date and time of the orderable procedure. This field is updated when the procedure is received into its performing service resource. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANG_ID` | [MIC_REF_ANG_REPORT](MIC_REF_ANG_REPORT.md) | `ANG_ID` |
| `ANG_NEG_SEQ` | [MIC_REF_ANG_REPORT](MIC_REF_ANG_REPORT.md) | `AUTO_NEG_SEQ` |
| `ANG_RUN_ID` | [MIC_ANG_STATUS](MIC_ANG_STATUS.md) | `ANG_RUN_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `INSTR_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `ORDER_ID` | [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `ORDER_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

