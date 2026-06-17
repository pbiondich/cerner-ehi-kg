# CNT_DTA

> DTA

**Description:** CNT DTA  
**Table type:** REFERENCE  
**Primary key:** `CNT_DTA_ID`  
**Columns:** 50  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies a specific activity type associated with the discrete task assay. |
| 3 | `ACTIVITY_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 4 | `BB_RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value used to determine result processing during blood bank result entry. |
| 5 | `BB_RESULT_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier from the CNT_CODE_VALUE_KEY table |
| 6 | `CERNER_DEFINED_IND` | DOUBLE | NOT NULL |  | (currently not implemented) |
| 7 | `CNT_DTA_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `CNT_DTA_KEY_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY VALUE FROM |
| 9 | `CNT_DTA_KEY_TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Not used |
| 10 | `CODE_SET` | DOUBLE | NOT NULL |  | Defines which code set is to be prompted for when the discrete task assay is defined as a result type of 'online' code set. |
| 11 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Concept CKI is the functional Concept Identifier; it is the codified means within Cerner Millennium? to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. Composed of a source and an identifier. For example, if the concept source is "SNOMED" and the conceptidentifier is "123", then the CKI is "SNOMED!123" |
| 12 | `DEFAULT_RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the default result type for the discrete task assay. |
| 13 | `DEFAULT_RESULT_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier from the CNT_CODE_VALUE_KEY table |
| 14 | `DEFAULT_TYPE_FLAG` | DOUBLE | NOT NULL |  | 0.00 No defaults 1.00 Default form the Reference Range 2.00 Default the last charted value 3.00 Default from the template script |
| 15 | `DELTA_LVL_FLAG` | DOUBLE | NOT NULL |  | 0.00 No delta checking 1.00 Perform delta checking on current result 2.00 Perform delta checking on current and previous result |
| 16 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Stores the long description for the discrete task assay. |
| 17 | `DTA_CKI` | VARCHAR(50) | NOT NULL |  | Cerner Knowledge Index for the code value |
| 18 | `DTA_INTERNAL_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for client created DTA |
| 19 | `EVENT_CD` | DOUBLE | NOT NULL |  | Cerner Knowledge Index for the code value. |
| 20 | `EVENT_CODE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier from the CNT_CODE_VALUE_KEY table |
| 21 | `HISTORY_ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | CODE SET 233 |
| 22 | `HISTORY_ACTIVITY_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier from the CNT_CODE_VALUE_KEY table |
| 23 | `ICD_CODE_IND` | DOUBLE | NOT NULL |  | indicates whether icd9 billing codes are associated with the discrete task assay. |
| 24 | `INTERP_DATA_IND` | DOUBLE | NOT NULL |  | indicates whether interpretive data is associated with the discrete task assay. |
| 25 | `IO_FLAG` | DOUBLE | NOT NULL |  | 0.00 Undetermined 1.00 Input 2.00 Output |
| 26 | `LABEL_TEMPLATE_ID` | DOUBLE | NOT NULL |  | ID of the dynamic label template which is updated from doc set import script(Request#4170080) |
| 27 | `MNEMONIC` | VARCHAR(50) |  |  | Defines the abbreviated form of the discrete task assay long description. Used in most applications to display the discrete assay task. |
| 28 | `MNEMONIC_KEY_CAP` | VARCHAR(50) |  |  | defines the discrete task assay mnemonic in uppercase. used for performing indexed searches on the table. |
| 29 | `MODIFIER_IND` | DOUBLE | NOT NULL |  | a normalized value which tells that a modifier that can be documented (extended description of the result) exists for the result. |
| 30 | `PRINT_REF_RANGES_ON_REPT_IND` | DOUBLE | NOT NULL |  | (currently not implemented) |
| 31 | `PRINT_RESULTS` | DOUBLE |  |  | (currently not implemented) |
| 32 | `RAD_SECTION_TYPE_CD` | DOUBLE | NOT NULL |  | Classifies the type of report section to which the procedure belongs. |
| 33 | `RAD_SECTION_TYPE_CDUID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** - REPLACED BY RAD_SECT_TYPE_CDUID *** Unique identifier from the CNT_CODE_VALUE_KEY table |
| 34 | `RAD_SECT_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier from the CNT_CODE_VALUE_KEY table |
| 35 | `REF_RANGE_SCRIPT` | VARCHAR(50) |  |  | defines an alternate site-specific script used to determine reference ranges for the discrete task assay. (currently not implemented) |
| 36 | `REL_ASSAY_IND` | DOUBLE | NOT NULL |  | indicates whether or not the discrete task assay has associated related discrete task assays defined. |
| 37 | `RENDERING_PROVIDER_IND` | DOUBLE | NOT NULL |  | (currently not implemented) |
| 38 | `SCI_NOTATION_IND` | DOUBLE | NOT NULL |  | this field indicates whether the task assay allows numeric values in scientific notation. if set, any value that exceeds the maximum digits and decimal places data map settings will be formatted in scientific notation. (e.g. maxdigits = 5, decimalplaces = 2, value = 1000.00 then formattedvalue = 1.00e3). otherwise, the value will be formatted using |
| 39 | `SIGNATURE_LINE_IND` | DOUBLE | NOT NULL |  | indicates whether the discrete task assay should have an associated signature line. |
| 40 | `SINGLE_SELECT_IND` | DOUBLE | NOT NULL |  | indicator for first alpha single select. for multi select dta, this indicator is used to make the first entry single select. |
| 41 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL |  | used to map to the strt_assay table for mdi database building. |
| 42 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 43 | `TASK_REPT_IND` | DOUBLE | NOT NULL |  | (currently not implemented) |
| 44 | `TRANSMIT_IND` | DOUBLE | NOT NULL |  | (currently not implemented) |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 50 | `VERSION_NUMBER` | DOUBLE |  |  | this tells the how many times a user has update the discrete_task_assay table. this table is not version-able and doesn't need to be versioned but we can store the versions in an archive so that we can compare what existed when it was documented. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_DTA_KEY_ID` | [CNT_DTA_KEY2](CNT_DTA_KEY2.md) | `CNT_DTA_KEY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CNT_DTA_RRF_R](CNT_DTA_RRF_R.md) | `CNT_DTA_ID` |

