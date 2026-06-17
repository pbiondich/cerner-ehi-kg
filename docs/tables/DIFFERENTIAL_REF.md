# DIFFERENTIAL_REF

> Defines the parameters used in result entry for counting a differential cell count.

**Description:** Differential Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_CORRECT_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific discrete task assay to be corrected automatically after a specified number of non-total cells has been exceeded. |
| 2 | `AUTO_CORRECT_IND` | DOUBLE |  |  | Indicates whether automatic correction is defined. A value of 0 indicates no automatic correction is defined. A value of 1 indicates an automatic correction is defined. |
| 3 | `AUTO_CORRECT_VALUE` | DOUBLE |  |  | Defines the number of non-total cells that need to be counted in order to invoke the automatic correction of the white blood count. |
| 4 | `AUTO_CORRECT_VERF_IND` | DOUBLE | NOT NULL |  | Indicates whether the status of the autocorrect procedure will be changed automatically to Corrected if it was verified previously. A value of 0 indicates no automatic correction of a verified result is defined. A value of 1 indicates an automatic correction of a verified result is defined. |
| 5 | `AUTO_CRCT_CMT` | VARCHAR(200) |  |  | Defines a free text comment to be appended to the footnote of the corrected procedure when the result entry application automatically corrects a result. |
| 6 | `AUTO_CRCT_CMT_IND` | DOUBLE |  |  | Indicates whether the automatic correct comment exists. A value of 0 indicates the automatic correct comment does not exist. A value of 1 indicates the automatic correct comment does exist. |
| 7 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the specific order catalog procedure for which differential counting will be performed. |
| 8 | `COUNT_LABEL` | VARCHAR(30) |  |  | Defines the label to be displayed over the counting column of the differential result entry function. |
| 9 | `DEFAULT_COUNT` | DOUBLE |  |  | Defines the default number of cells to be counted for a given differential cell count. |
| 10 | `DIF_REF_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific differential reference row. |
| 11 | `INSTR_LABEL` | VARCHAR(30) |  |  | Defines the label to be displayed above the instrument section of the differential result entry application. |
| 12 | `MORPH_LABEL` | VARCHAR(30) |  |  | Defines the label to be displayed above the morphology section of the differential result entry application. |
| 13 | `NORMALIZE_IND` | DOUBLE |  |  | Indicates whether the cell count should be normalized to 100. A value of 0 indicates the cell count will not be normalized to 100. A value of 1 indicates the cell count will be normalized to 100. |
| 14 | `OPT` | VARCHAR(20) |  |  | Stores the option description for display and selection. |
| 15 | `OPT_KEY` | VARCHAR(20) |  |  | Stores the option in uppercase for checking duplicates and sorting. |
| 16 | `SUBTRACT_KEY` | CHAR(1) |  |  | Defines the key used to invoke the subtraction mode for differential cell counting in result entry. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

