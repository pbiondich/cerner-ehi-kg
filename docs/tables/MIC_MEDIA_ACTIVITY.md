# MIC_MEDIA_ACTIVITY

> This table contains media activity information for each orderable procedure.

**Description:** Microbiology Blood Analyzer Media Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 2 | `FINAL_UNLOAD_DT_TM` | DATETIME |  |  | This field identifies the date and time the media was unloaded from the blood culture instrument. This date and time is sent to the Cerner system from several of the blood culture instrument interfaces. This date and time is used to know when the Cerner system should send the final ANG report defined to be sent at 9999 hours. |
| 3 | `INITIAL_LOAD_DT_TM` | DATETIME |  |  | This field identifies the date and time the media was actually loaded onto the blood culture instrument. This date and time is sent to the Cerner system from several of the blood culture instrument interfaces. This date and time is used to calculate the ANG reporting times. |
| 4 | `INSTR_MEDIA_IDENT` | VARCHAR(50) |  |  | Identification number assigned to media uploaded from automated microbiology instruments. |
| 5 | `INSTR_MEDIA_LOCATION` | CHAR(10) |  |  | This field identifies the exact location of the media in the instrument. |
| 6 | `INSTR_STATUS` | CHAR(20) |  |  | This field is not used at this time. |
| 7 | `INSTR_TRANS` | CHAR(15) |  |  | This field identifies the translation code for the media. This is the code that will be sent to the blood culture instrument interface to represent the type of media. |
| 8 | `LABEL_CNT` | DOUBLE |  |  | This field identifies the number of media labels to be printed for this type of media. |
| 9 | `LAST_RESULT_DT_TM` | DATETIME |  |  | This field identifies the date and time the last result was received from the blood culture instrument interface. |
| 10 | `LAST_RESULT_FLAG` | DOUBLE |  |  | This field indicates the type of transaction sent from the instrument. |
| 11 | `MEDIA_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value of the specific type of media identified for this procedure. Media types are defined on code set 2051 Specimen Containers. |
| 12 | `MEDIA_SEQ` | DOUBLE | NOT NULL |  | This field contains a unique value that uniquely identifies more than occurrence of the same media code for a given organism. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 14 | `POSITIVE_DT_TM` | DATETIME |  |  | This field identifies the date and time the Cerner system last received a positive transaction on this media. |
| 15 | `POSITIVE_IND` | DOUBLE |  |  | This field identifies that the Cerner system has received a presumptive positive transaction from the instrument for this type of media. This indicator does not set the orderable procedure to positive. Only positive responses and/or organisms issued as part of a preliminary, final or amended report type can set an orderable procedure to positive. |
| 16 | `START_DT_TM` | DATETIME |  |  | This field identifies the start date and time of the orderable procedure. This field is updated when the procedure is received into its performing service resource. |
| 17 | `START_ID` | DOUBLE | NOT NULL |  | This field identifies the ID of the person who started the procedure. The start_id corresponds to the person_id on the prsnl table, which identifies the user. |
| 18 | `SUBCULTURE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 19 | `TASK_LOG_ID` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `MEDIA_CD` | [MIC_MEDIA](MIC_MEDIA.md) | `MEDIA_CD` |
| `ORDER_ID` | [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `ORDER_ID` |

