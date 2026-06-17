# HF_D_HOSPITAL

> This is the HealthFacts dimension table that contains HealthFacts recognized hospitals for all health systems

**Description:** health facts dimension hospital  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACUTE_IND` | DOUBLE |  |  | Indicates if the facility is an acute or non-acute care facility |
| 2 | `ACUTE_STATUS` | VARCHAR(20) |  |  | Indicated whether the facility is an acute or non-acute care facility. |
| 3 | `ALT_HEALTH_SYSTEM_ID` | DOUBLE |  |  | The unique Health System Identifier for the alternative hospital. |
| 4 | `ALT_HOSPITAL_ID` | DOUBLE |  |  | The unique identifier for the alternative hospital. |
| 5 | `BED_SIZE_RANGE` | VARCHAR(10) |  |  | Gives the approximate number of beds in a hospital. |
| 6 | `CATH_LAB_DIAGNOSTIC_IND` | DOUBLE |  |  | Indicates whether the facility has a diagnostic Catheterization laboratory |
| 7 | `CATH_LAB_FULL_IND` | DOUBLE |  |  | Indicates whether the facility has a full Catheterization laboratory |
| 8 | `CENSUS_DIVISION` | VARCHAR(40) |  |  | Specifies which of the 9 census divisions (New England, Middle Atlantic, West North Central, East North Central, East South Central, South Atlantic, West South Central, Mountain, Pacific) the facility is located in |
| 9 | `CENSUS_REGION` | VARCHAR(40) |  |  | Specifies which of the four census regions (Northeast, Midwest, South, West) the facility is located in |
| 10 | `CLIA_NBR` | VARCHAR(10) |  |  | The CLIA number associated with the facility |
| 11 | `COUNTY_FIPS_CODE` | VARCHAR(10) |  |  | The FIPS county code is a three-digit Federal Information Processing Standard (FIPS) code (FIPS 6-4) which uniquely identifies counties and county equivalents in the United States, certain U.S. possessions, and certain freely associated states. The first two digits are the FIPS state code and the last three are the county code within the state or possession. |
| 12 | `CREATE_PSP_REPORT_IND` | DOUBLE |  |  | Indicates if the facility should have PSP reports created |
| 13 | `DEFAULT_FACILITY_IND` | DOUBLE |  |  | Indicates that this is the default facility for the hospital. |
| 14 | `DIRECTOR_FIRST_NAME` | VARCHAR(100) |  |  | The first name of the Director of the hospital. |
| 15 | `DIRECTOR_LAST_NAME` | VARCHAR(100) |  |  | The last name of the Director of the hospital. |
| 16 | `DIRECTOR_MIDDLE_NAME` | VARCHAR(100) |  |  | The middle name of the Director of the hospital. |
| 17 | `DIRECTOR_PREFIX` | VARCHAR(10) |  |  | The prefix of the Director of the hospital. |
| 18 | `DIRECTOR_SUFFIX` | VARCHAR(10) |  |  | The suffix of the Director of the hospital. |
| 19 | `DIRECTOR_TITLE` | VARCHAR(10) |  |  | The title of the Director of the hospital. |
| 20 | `HEALTHFACTS_IND` | DOUBLE |  |  | This is an indicator 0 (no) or 1 (yes) if this is to be used for Health Data (Health Facts or HealthSentry) mapping purposes. |
| 21 | `HEALTHSENTRY_IND` | DOUBLE |  |  | This is an indicator 0 (no) or 1 (yes) if this is to be used for Health Data (Health Facts or HealthSentry) mapping purposes. |
| 22 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | The health system that the hospital belongs to |
| 23 | `HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | Address of the hospital |
| 24 | `HOSPITAL_ADDRESS_2` | VARCHAR(100) |  |  | The second line of address for the hospital. |
| 25 | `HOSPITAL_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | The documented instructions for how to contact the hospital. |
| 26 | `HOSPITAL_CBSA` | VARCHAR(25) |  |  | Core Based Statistical Area for the hospital. http://www.zip-codes.com/. Look up the zip code to find the CBSA. |
| 27 | `HOSPITAL_CITY` | VARCHAR(100) |  |  | City of the hospital |
| 28 | `HOSPITAL_CODE` | DOUBLE |  |  | A Millennium identifier for the hospital |
| 29 | `HOSPITAL_COUNTRY` | VARCHAR(100) |  |  | The country in which the hospital resides. |
| 30 | `HOSPITAL_COUNTY` | VARCHAR(100) |  |  | The county in which the hospital resides. |
| 31 | `HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display value of the hospital. |
| 32 | `HOSPITAL_EXTENSION` | VARCHAR(100) |  |  | The phone extension for the hospital. |
| 33 | `HOSPITAL_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines an isolate |
| 34 | `HOSPITAL_NAME` | VARCHAR(255) |  |  | Name of the hospital |
| 35 | `HOSPITAL_OID` | VARCHAR(100) |  |  | The OID of the hospital. |
| 36 | `HOSPITAL_PHONE` | VARCHAR(30) |  |  | Phone number for the hospital |
| 37 | `HOSPITAL_STATE` | VARCHAR(50) |  |  | State of the hospital |
| 38 | `HOSPITAL_ZIP` | VARCHAR(25) |  |  | Zipcode of the hospital |
| 39 | `INSTITUTION_REF` | VARCHAR(40) |  |  | Code value that defines that institution. This field is used in conjunction with Health_System_ID to join activity data to this table. |
| 40 | `NPI` | VARCHAR(10) |  |  | National Provider Identifier (NPI) is a Health Insurance Portability and Accountability Act (HIPAA) Administrative Simplification Standard. The NPI is a unique identification number for covered health care providers. |
| 41 | `PERFORM_FACILITY_IND` | DOUBLE |  |  | Indicates that this is a performing facility for the hospital. |
| 42 | `STATE_FIPS_CODE` | VARCHAR(10) |  |  | The FIPS State code is a two-digit Federal Information Processing Standard (FIPS) code (FIPS 6-4) which uniquely identifies States and State equivalents in the United States, certain U.S. possessions, and certain freely associated states. |
| 43 | `TEACHING_FACILITY_IND` | DOUBLE |  |  | Indicates if the facility is a teaching facility |
| 44 | `TOTAL_BEDS` | DOUBLE |  |  | Number of beds in a hospital. Only populated for HealthSentry |
| 45 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 46 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 47 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |
| 48 | `URBAN_RURAL_STATUS` | VARCHAR(20) |  |  | Urban or rural indicator for this facility. U (Urban), R (Rural) |
| 49 | `URBAN_RURAL_STATUS_IND` | DOUBLE |  |  | Indicates if the facility is in an urban or rural area |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

