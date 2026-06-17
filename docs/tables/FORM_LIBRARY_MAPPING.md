# FORM_LIBRARY_MAPPING

> Maps the form library configuration of the printer to the its printer device

**Description:** FORM LIBRARY MAPPIG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COPIES_NBR` | DOUBLE |  |  | The amount of copies |
| 2 | `FORM_LIBRARY_ID` | DOUBLE |  | FK→ | The ID of the default form library for the printer |
| 3 | `FORM_LIBRARY_MAPPING_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `OUTPUT_DISABLED_IND` | DOUBLE |  |  | Indicates if the given mapping will disable printer output. Default of off. |
| 5 | `PRINTER_ID` | DOUBLE |  | FK→ | The DEVICE_CD of the mapped printer |
| 6 | `REDIRECT_PRINTER_ID` | DOUBLE |  | FK→ | The DEVICE_CD of the redirect printer; |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORM_LIBRARY_ID` | [FORM_LIBRARY](FORM_LIBRARY.md) | `FORM_LIBRARY_ID` |
| `PRINTER_ID` | [DEVICE](DEVICE.md) | `DEVICE_CD` |
| `REDIRECT_PRINTER_ID` | [DEVICE](DEVICE.md) | `DEVICE_CD` |

