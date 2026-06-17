# MIC_ANG_TIMES

> This table contains information regarding the times of the day when the automatic no growth reporting process should issue reports.

**Description:** Microbiology Automatic No Growth Times  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 2 | `DAY_OF_WEEK` | DOUBLE | NOT NULL |  | This field identifies the day of the week for which automatic no growth reporting are defined. Valid values include: 1 = Sunday 2 = Monday 3 = Tuesday 4 = Wednesday 5 = Thursday 6 = Friday 7 = Saturday |
| 3 | `PERFORM_ONLY_IND` | DOUBLE |  |  | This field indicates if the reports issued via the automatic no growth process should be performed or verified. Valid values include: 0 = Verify the reports 1 = Perform the reports |
| 4 | `PRINTER_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the printer where the ANG summary report should be printed.This field corresponds to the output destination code of the printer from the output destination table. |
| 5 | `PRINT_RPT_IND` | DOUBLE |  |  | This field indicates if a automatic no growth summary report should be generated for the specified time. Valid values include: 0 = Do not print the summary report 1 = Print the summary report |
| 6 | `RUN_IND` | DOUBLE |  |  | This field indicates if the automatic no growth process should activate and run for the time specified. Valid values include: 0 = Do not run 1 = Run |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the instrument or bench for which automatic no growth times are defined. |
| 8 | `TIME_SEQ` | DOUBLE | NOT NULL |  | This field indicates the time of day as a number between 1 and 24 as shown below: 00:00 = 1 01:00 = 2 02:00 = 3 03:00 = 4 04:00 = 5 05:00 = 6 06:00 = 7 07:00 = 8 08:00 = 9 09:00 = 10 10:00 = 11 11:00 = 12 12:00 = 13 13:00 = 14 14:00 = 15 15:00 = 16 16:00 = 17 17:00 = 18 18:00 = 19 19:00 = 20 20:00 = 21 21:00 = |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `PRINTER_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

