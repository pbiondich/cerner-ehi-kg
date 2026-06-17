# BR_AUTO_ORDER_CATALOG

> autobuild orderables

**Description:** BEDROCK AUTO ORDER CATALOG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | activity sub type |
| 2 | `ACTIVITY_SUBTYPE_DISPLAY` | VARCHAR(40) |  |  | If the cdf meaning doesn't exist for the subactivity type define this field with the display value |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | activity type |
| 4 | `ACTIVITY_TYPE_DISPLAY` | VARCHAR(40) |  |  | Display of the activity type |
| 5 | `BB_PROCESSING_CD` | DOUBLE | NOT NULL |  | procedure type associated to the Blood Bank order |
| 6 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 7 | `CARDIOLOGY_IND` | DOUBLE |  |  | Indicates whether order can be accessed by Cardiology |
| 8 | `CATALOG_CD` | DOUBLE | NOT NULL |  | order catalog id |
| 9 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | order catalog type |
| 10 | `CATALOG_TYPE_DISPLAY` | VARCHAR(40) |  |  | Display of the catalog type |
| 11 | `CKI` | VARCHAR(255) |  |  | Cerner knowledge index |
| 12 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Concept CKI associated to the order catalog item. |
| 13 | `CPT4` | VARCHAR(25) |  |  | cpt4 code |
| 14 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | The clinical category associated to the order catalog item. |
| 15 | `DEPT_NAME` | VARCHAR(100) |  |  | Department name for the order catalog item. |
| 16 | `DESCRIPTION` | VARCHAR(100) |  |  | Description for the order catalog item. |
| 17 | `LABORATORY_IND` | DOUBLE |  |  | Indicates whether order can be accessed by Laboratory |
| 18 | `LOINC` | VARCHAR(10) |  |  | loinc code |
| 19 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | Order entry format associated to the order catalog item. |
| 20 | `PATIENT_CARE_IND` | DOUBLE |  |  | Indicates whether order can be accessed by Patient Care |
| 21 | `PRIMARY_MNEMONIC` | VARCHAR(100) | NOT NULL |  | Primary mnemonic for the order catalog item |
| 22 | `RADIOLOGY_IND` | DOUBLE |  |  | Indicates whether order can be accessed by Radiology |
| 23 | `SURGERY_IND` | DOUBLE |  |  | Indicates whether order can be accessed by Surgery |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

