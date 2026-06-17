# LH_QRDA_MEDICATION

> This table is used to store elements that are used to create the Medication Section in the body of a QRDA file for submission

**Description:** LH_QRDA_MEDICATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 54

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOSE_QUANTITY` | VARCHAR(50) |  |  | Units of medication to take per administration |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 5 | `FREQUENCY` | VARCHAR(50) |  |  | Indicates the frequency (in hours) of administration |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LH_QRDA_MEDICATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_MEDICATION table. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `MEDICATION_DT_TM` | DATETIME |  |  | Indicates the actual or intended time of administration/dispensing of medication |
| 12 | `MEDICATION_END_DT_TM` | DATETIME |  |  | The date/time the record was end date for medication order into the table. |
| 13 | `MEDICATION_END_OFFSET_UTC` | VARCHAR(6) |  |  | MEDICATION_END_OFFSET_UTC stores UTC offset for MEDICATION_END_DT_TM |
| 14 | `MEDICATION_OFFSET_UTC` | VARCHAR(6) |  |  | MEDICATION_OFFSET_UTC stores UTC offset for MEDICATION_DT_TM |
| 15 | `MEDICATION_TEMPLATE` | VARCHAR(50) |  |  | Type of medication. Example: Medication Order, Medication Active, Medication Allergy, Medication Intolerance etc. |
| 16 | `MEDS_DISPENSE_QTY` | DOUBLE |  |  | This field contains the dispense quantity of the medication. |
| 17 | `MEDS_DISPENSE_QTY_UNIT` | VARCHAR(100) |  |  | This field contains the unit of the dispense quantity of medication. |
| 18 | `MEDS_DURATION` | DOUBLE |  |  | This field contains the duration for medication. |
| 19 | `MEDS_DURATION_UNIT` | VARCHAR(100) |  |  | This field contains the unit for duration of the medication. |
| 20 | `MEDS_FREQUENCY` | DOUBLE |  |  | This field contains the frequency of the medication. |
| 21 | `MEDS_REFILL_CNT` | DOUBLE |  |  | This field contains the refill count of the medication. |
| 22 | `MEDS_STRENGTH_DOSE` | DOUBLE |  |  | This field contains medication dose's strength. |
| 23 | `MEDS_STRENGTH_DOSE_UNIT` | VARCHAR(100) |  |  | This field contains the unit of the medication dose's strength. |
| 24 | `MEDS_VOLUME_DOSE` | DOUBLE |  |  | This field contains medication dose's volume. |
| 25 | `MEDS_VOLUME_DOSE_UNIT` | VARCHAR(100) |  |  | This field contains the unit of the medication dose's volume. |
| 26 | `MED_ID` | DOUBLE | NOT NULL |  | Unique medication id |
| 27 | `MED_STATUS_CODE` | VARCHAR(50) |  |  | Represents the status of the medication. |
| 28 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether a negation exists or not |
| 29 | `NEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time when the negation was recorded |
| 30 | `NEG_PRODUCT_CODE` | VARCHAR(50) |  |  | CMS code that describes the negation |
| 31 | `NEG_PRODUCT_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system from which neg_product_code was derived from |
| 32 | `NEG_PRODUCT_DISPLAY` | VARCHAR(500) |  |  | Text description of the negation |
| 33 | `OBS_CODE_NEG` | VARCHAR(50) |  |  | Represents a given code value (not Cerner's code value) from obs_cd_system (negation) |
| 34 | `OBS_CODE_SYSTEM_NAME_NEG` | VARCHAR(50) |  |  | The name of the result's code system (negation) (e.g. SNMCT) |
| 35 | `OBS_CODE_SYSTEM_NEG` | VARCHAR(50) |  |  | Represents the codeSystem string of the code node (negation) |
| 36 | `OBS_CODE_SYSTEM_SDTC_NEG` | VARCHAR(50) |  |  | The OID of the code system's value set |
| 37 | `OBS_DISPLAY_NEG` | VARCHAR(500) |  |  | Text representation of the result (negation) |
| 38 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Medication section is related (i.e. lh_qrda_pqrs_id) |
| 39 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The name of millennium source table |
| 40 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table this Medication section is related (i.e. LH_QRDA_PQRS) |
| 41 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The value of the primary identifier of millennium source table |
| 42 | `PRODUCT_CODE` | VARCHAR(50) |  |  | Code that describes the product/medication |
| 43 | `PRODUCT_CODE_SYSTEM` | VARCHAR(50) |  |  | Code system from which product_cd was derived from |
| 44 | `PRODUCT_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the result's code system (e.g. SNMCT) |
| 45 | `PRODUCT_CODE_SYSTEM_SDTC` | VARCHAR(50) |  |  | The OID of the code system's value set |
| 46 | `PRODUCT_DISPLAY` | VARCHAR(500) |  |  | Text description of the product |
| 47 | `PRODUCT_FULL_DISPLAY` | VARCHAR(500) |  |  | Full length text description of the product |
| 48 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 49 | `ROUTE_CODE` | VARCHAR(50) |  |  | Code describing the route of administration |
| 50 | `SUPPLY_IND` | DOUBLE |  |  | Indicates whether the activity is a SubstanceAdministration (medication activity) or Supply (supply activity). 0 indicates medication activity and 1 indicates supply activity |
| 51 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 54 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

