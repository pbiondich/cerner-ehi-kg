# EEM_PROFILE

> EEM profile table

**Description:** EEM profile.  
**Table type:** REFERENCE  
**Primary key:** `PROFILE_ID`  
**Columns:** 124  
**Referenced by:** 16 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_FUTURE_IND` | DOUBLE | NOT NULL |  | Allow future indicator (yes (1) or No (0)) |
| 3 | `ALLOW_HISTORIC_IND` | DOUBLE | NOT NULL |  | Allow historic indicator (yes (1) or No (0)) |
| 4 | `ALLOW_PROCEDURE_LVL_IND` | DOUBLE | NOT NULL |  | Allow Procedure level indicator (yes (1) or No (0)) |
| 5 | `ALLOW_SERVICE_TYPE_LVL_IND` | DOUBLE | NOT NULL |  | Allow service type level indicator (yes (1) or No (0)) |
| 6 | `AUTOMATION_FLAG` | DOUBLE | NOT NULL |  | The type of automation used. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CONTACT` | VARCHAR(100) |  |  | Contact. |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `DATA_DURATION` | DOUBLE | NOT NULL |  | Duration, in number of seconds, in which data should remain available. |
| 11 | `DATA_DURATION_FLAG` | DOUBLE | NOT NULL |  | The type of data duration. 0 - Message not returned, 1 - Message returned (eligible), 1 - Message returned (not eligible), 3 - Message returned (Unknown or non-eligibility message), 4 - Message returned (error), 5 - Message template. |
| 12 | `DEFAULT_SVC_TYPE_CD` | DOUBLE | NOT NULL |  | The default service type. |
| 13 | `DEP_UNIQ_ID_CD` | DOUBLE | NOT NULL |  | Indicates if this profile has dependents that are uniquely identifiable -No HL23 |
| 14 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of profile. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `GS_APP_RECEIVERS_CODE` | VARCHAR(15) |  |  | Data to be placed in the outbound field.. GS-03 |
| 17 | `GS_APP_SENDERS_CODE` | VARCHAR(15) |  |  | Data to be placed in the outbound field.. GS-02 |
| 18 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The ID of the health plan associated with the profile. |
| 19 | `INFOSOURCE_COMM_NUM1` | VARCHAR(80) |  |  | Requester's first communication number for contacting the requester. |
| 20 | `INFOSOURCE_COMM_NUM1_CD` | DOUBLE | NOT NULL |  | Requester's first communication number qualifier code for the requester (email, fax, phone). |
| 21 | `INFOSOURCE_COMM_NUM2` | VARCHAR(80) |  |  | Requester's second communication number for contacting the requester. |
| 22 | `INFOSOURCE_COMM_NUM2_CD` | DOUBLE | NOT NULL |  | Requester's second communication number qualifier code for the requester (email, fax, phone, extension). |
| 23 | `INFOSOURCE_COMM_NUM3` | VARCHAR(80) |  |  | Requester's third communication number for contacting the requester. |
| 24 | `INFOSOURCE_COMM_NUM3_CD` | DOUBLE | NOT NULL |  | Requester's third communication number qualifier code for the requester (email, fax, phone, extension). |
| 25 | `INFOSOURCE_CONTACT_NAME` | VARCHAR(60) |  |  | Requester's contact Name for the requester of the authorization transaction. |
| 26 | `INFOSOURCE_ENTITY_ID_CD` | DOUBLE | NOT NULL |  | Data to be placed in the outbound field.. NM1-01. |
| 27 | `INFOSOURCE_ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | Data to be placed in the outbound field.. NM1-02. |
| 28 | `INFOSOURCE_ID_CD` | DOUBLE | NOT NULL |  | Data to be placed in the outbound field.. NM1-08. |
| 29 | `INFOSOURCE_NAME_FIRST` | VARCHAR(35) |  |  | Data to be placed in the outbound field.. HL-20 -> NM1-04 (If NM1-02 has a "1"). |
| 30 | `INFOSOURCE_NAME_LAST_ORG` | VARCHAR(60) |  |  | Data to be placed in the outbound field.. NM1-03. |
| 31 | `INFOSOURCE_NAME_MIDDLE` | VARCHAR(25) |  |  | Data to be placed in the outbound field.. NM1-05. |
| 32 | `INFOSOURCE_NAME_SUFFIX` | VARCHAR(10) |  |  | Data to be placed in the outbound field.. NM1-07. |
| 33 | `INFOSOURCE_PRIMARY_IDEN` | VARCHAR(80) |  |  | Data to be placed in the outbound field.. NM1-09 (Qualified by NM1-08). |
| 34 | `INITIAL_DELAY` | DOUBLE | NOT NULL |  | The number of seconds to wait before any polling should take place. |
| 35 | `ISA_ACK_REQUESTED_CD` | DOUBLE | NOT NULL |  | Data to be placed in the outbound field.. ISA-14. |
| 36 | `ISA_AUTHOR_INFORMATION` | VARCHAR(10) |  |  | Data to be placed in the outbound field.. ISA-02. |
| 37 | `ISA_AUTHOR_INFO_QUAL_CD` | DOUBLE | NOT NULL |  | ISA-01 |
| 38 | `ISA_INTERCHG_REC_IDEN` | VARCHAR(15) |  |  | Data to be placed in the outbound field.. ISA-08. |
| 39 | `ISA_INTERCHG_REC_ID_QUAL_CD` | DOUBLE | NOT NULL |  | Data to be placed in the outbound field.. ISA-07. |
| 40 | `ISA_INTERCHG_SENDER_IDEN` | VARCHAR(15) |  |  | Data to be placed in the outbound field. ISA-06. |
| 41 | `ISA_INTERCHG_SENDER_ID_QUAL_CD` | DOUBLE | NOT NULL |  | Data to be placed in the outbound field.. ISA-05 |
| 42 | `ISA_SECURITY_INFORMATION` | VARCHAR(10) |  |  | Data to be placed in the outbound field.. ISA-04. |
| 43 | `ISA_SECURITY_INFO_QUAL_CD` | DOUBLE | NOT NULL |  | Data to be placed in the outbound field.ISA-03. |
| 44 | `MAX_DELAY` | DOUBLE | NOT NULL |  | The maximum number of seconds to wait before timing out transactions. |
| 45 | `MAX_RESUBMIT_DURATION` | DOUBLE | NOT NULL |  | The maximum re-submit duration defines the length of time after a transaction was first submitted and the last time the transaction service should attempt a resubmit if necessary. |
| 46 | `MOH_FACILITY` | VARCHAR(30) |  |  | Ministry issues values for facility identification |
| 47 | `MOH_LOCAL_DEVICE` | VARCHAR(30) |  |  | Identifies where the transaction came from a facility (e.g., Emergency Department |
| 48 | `MOH_LOCAL_USER` | VARCHAR(30) |  |  | Contains the client's authorization ID. |
| 49 | `MOH_PROVIDER` | VARCHAR(30) |  |  | Ministry issued values for provider identification. |
| 50 | `MOH_TRANSACTION` | VARCHAR(30) |  |  | RPVR0500 followed by a space |
| 51 | `MOH_USER` | VARCHAR(30) |  |  | Authorization issues by the ministry |
| 52 | `PASSWORD` | VARCHAR(40) |  |  | Foreign system password. |
| 53 | `PAYOR_ID` | DOUBLE | NOT NULL | FK→ | Organization ID of payor. |
| 54 | `POLL_DELAY` | DOUBLE | NOT NULL |  | Number of seconds to wait between polls. |
| 55 | `POLL_DURATION` | DOUBLE | NOT NULL |  | Number of seconds an incomplete transaction is available for polling. |
| 56 | `PROFILE_ID` | DOUBLE | NOT NULL | PK | The primary ID of this table. |
| 57 | `PROXY_FLAG` | DOUBLE | NOT NULL |  | Indicates whether data is proxy hosted. 0 - Not proxy hosted, 1 - Proxy hosted. |
| 58 | `RP_COMM_NUM1` | VARCHAR(256) |  |  | First communication number for contacting the requester. |
| 59 | `RP_COMM_NUM1_CD` | DOUBLE | NOT NULL |  | First communication number qualifier code for the requester (email, fax, phone). |
| 60 | `RP_COMM_NUM2` | VARCHAR(256) |  |  | Second communication NUMBER FOR contacting the requester. |
| 61 | `RP_COMM_NUM2_CD` | DOUBLE | NOT NULL |  | Second communication NUMBER qualifier code FOR the requester (email, fax, phone, extension). |
| 62 | `RP_COMM_NUM3` | VARCHAR(256) |  |  | Third communication NUMBER FOR contacting the requester. |
| 63 | `RP_COMM_NUM3_CD` | DOUBLE | NOT NULL |  | Third communication NUMBER qualifier code FOR the requester (email, fax, phone, extension). |
| 64 | `RP_CONTACT_NAME` | VARCHAR(60) |  |  | Contact Name for the requester of the authorization transaction. |
| 65 | `RP_N3_ADDR1` | VARCHAR(55) |  |  | N3 segment address 1 (2100B N3-01). |
| 66 | `RP_N3_ADDR2` | VARCHAR(55) |  |  | N3 segment address 2 (2100B N3-02). |
| 67 | `RP_N4_CITY` | VARCHAR(30) |  |  | N4 segment city (2100B N4-01). |
| 68 | `RP_N4_COUNTRY_CODE` | VARCHAR(3) |  |  | N4 segment country code (2100B N4-04). |
| 69 | `RP_N4_POSTAL_CODE` | VARCHAR(15) |  |  | N4 segment postal code (2100B N4-03). |
| 70 | `RP_N4_STATE_PROV_CD` | DOUBLE | NOT NULL |  | N4 segment state/provential code (2100B N4-02). |
| 71 | `RP_NM1_ENTITY_ID_CD` | DOUBLE | NOT NULL |  | NM1-segment entity id code set (2100B NM1-01). |
| 72 | `RP_NM1_ENTITY_TYPE_QUAL_CD` | DOUBLE | NOT NULL |  | NM1-segment entity type qual code set (2100B NM1-02). |
| 73 | `RP_NM1_IDEN` | VARCHAR(80) |  |  | NM1 segment identification. |
| 74 | `RP_NM1_IDEN_CD` | DOUBLE | NOT NULL |  | NM1 segment identification code value (2100B NM1-09). |
| 75 | `RP_NM1_NAME_FIRST` | VARCHAR(35) |  |  | NM1 segment First Name (2100B NM1-04). |
| 76 | `RP_NM1_NAME_LAST_ORG` | VARCHAR(60) |  |  | NM1 segment last or organization Name (2100B NM1-03). |
| 77 | `RP_NM1_NAME_MIDDLE` | VARCHAR(25) |  |  | NM1 segment middle Name (2100B NM1-05). |
| 78 | `RP_NM1_NAME_SUFFIX` | VARCHAR(10) |  |  | NM1 segment suffix (2100B NM1-07). |
| 79 | `RP_PRV_PROV_CD` | DOUBLE | NOT NULL |  | PRV segment provider code value (2100B PRV-01). |
| 80 | `RP_PRV_REF_ID` | VARCHAR(50) |  |  | PRV segment reference identification code value (2100B PRV-02). |
| 81 | `RP_PRV_REF_ID_QUAL_CD` | DOUBLE | NOT NULL |  | PRV segment reference identification qual code value (2100B PRV-03). |
| 82 | `RP_REF_CARRIER_REF_NUM` | VARCHAR(50) |  |  | The carrier assigned reference NUMBER IS additional reference identification FOR the TRANSACTION requester. |
| 83 | `RP_REF_CONTRACT_NUM` | VARCHAR(50) |  |  | The REF segment contract number. |
| 84 | `RP_REF_CONTRACT_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment contract number. |
| 85 | `RP_REF_ELECT_DEV_PIN_NUM` | VARCHAR(50) |  |  | The pin number REF electronic device. |
| 86 | `RP_REF_ELECT_DEV_PIN_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF electronic device pin number. |
| 87 | `RP_REF_EMPLOYER_ID_NUM` | VARCHAR(50) |  |  | The employer id NUMBER IS additional reference identification FOR the TRANSACTION requester. |
| 88 | `RP_REF_FACILITY_ID_NUM` | VARCHAR(50) |  |  | The number of the REF segment facility. |
| 89 | `RP_REF_FACILITY_ID_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment facility id number. |
| 90 | `RP_REF_FAC_NETWK_ID_NUM` | VARCHAR(50) |  |  | The number of the REF segment facility network. |
| 91 | `RP_REF_FAC_NETWK_ID_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment facility network. |
| 92 | `RP_REF_FED_TAXPAYER_NUM` | VARCHAR(50) |  |  | The federal taxpayer number of the REF segment. |
| 93 | `RP_REF_FED_TAXPAYER_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment federal taxpayer number. |
| 94 | `RP_REF_HCFA_NAT_PROV_NUM` | VARCHAR(50) |  |  | The number of the REF segment HCFA national provider. |
| 95 | `RP_REF_HCFA_NAT_PROV_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment HCFA national provider number. |
| 96 | `RP_REF_MEDICAID_PRV_NUM` | VARCHAR(50) |  |  | The number of the REF segment Medicaid provider. |
| 97 | `RP_REF_MEDICAID_PRV_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment Medicaid provider number. |
| 98 | `RP_REF_MEDICARE_PRV_NUM` | VARCHAR(50) |  |  | The number of the REF segment Medicare provider. |
| 99 | `RP_REF_MEDICARE_PRV_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment Medicare provider number. |
| 100 | `RP_REF_PERS_ID_NUM` | VARCHAR(50) |  |  | The ID of the REF segment personal. |
| 101 | `RP_REF_PERS_ID_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment personal identification number. |
| 102 | `RP_REF_PRIOR_ID_NUM` | VARCHAR(50) |  |  | The ID of the REF segment prior. |
| 103 | `RP_REF_PRIOR_ID_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment prior number. |
| 104 | `RP_REF_PRV_PLN_NW_ID_NUM` | VARCHAR(50) |  |  | The ID of the REF segment provider plan network. |
| 105 | `RP_REF_PRV_PLN_NW_ID_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment provider plan network identification number. |
| 106 | `RP_REF_PRV_SITE_NUM` | VARCHAR(50) |  |  | The provider site number to be used in the REF segment within the Information Source loop. |
| 107 | `RP_REF_PRV_UPIN_NUM` | VARCHAR(50) |  |  | The provider UPIN NUMBER IS additional reference identification FOR the TRANSACTION requester. |
| 108 | `RP_REF_SSN` | VARCHAR(50) |  |  | The REF segment social security number. |
| 109 | `RP_REF_SSN_DESC` | VARCHAR(80) |  |  | The REF segment social security number description. |
| 110 | `RP_REF_STATE_LIC_NUM` | VARCHAR(50) |  |  | The REF segment State license number. |
| 111 | `RP_REF_STATE_LIC_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment State license number. |
| 112 | `RP_REF_SUBMITTER_ID_NUM` | VARCHAR(50) |  |  | The ID of the REF segment submitter. |
| 113 | `RP_REF_SUBMITTER_ID_NUM_DESC` | VARCHAR(80) |  |  | The description of the REF segment submitter ID number. |
| 114 | `RP_REF_USER_ID` | VARCHAR(50) |  |  | The ID of the REF segment user. |
| 115 | `RP_REF_USER_ID_DESC` | VARCHAR(80) |  |  | The description of the REF segment user ID. |
| 116 | `TRANSACTION_CD` | DOUBLE | NOT NULL |  | The type of transaction supported by this profile. |
| 117 | `TRANS_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of transaction. 0 - Single transaction submission only, 1 - Single or batch transaction submission. |
| 118 | `TRANS_VERSION_CD` | DOUBLE | NOT NULL |  | A codified attribute to define the transaction version supported |
| 119 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 120 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 121 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 122 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 123 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 124 | `USERNAME` | VARCHAR(40) |  |  | User name for foreign system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PAYOR_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (16)

| From table | Column |
|------------|--------|
| [EEM_ADDRESS_DETAIL](EEM_ADDRESS_DETAIL.md) | `PROFILE_ID` |
| [EEM_AUTH_DETAIL](EEM_AUTH_DETAIL.md) | `PROFILE_ID` |
| [EEM_COVERAGE_DETAIL](EEM_COVERAGE_DETAIL.md) | `PROFILE_ID` |
| [EEM_DEMOG_DETAIL](EEM_DEMOG_DETAIL.md) | `PROFILE_ID` |
| [EEM_ELIG_DETAIL](EEM_ELIG_DETAIL.md) | `PROFILE_ID` |
| [EEM_LOG](EEM_LOG.md) | `PROFILE_ID` |
| [EEM_MOH_DETAIL](EEM_MOH_DETAIL.md) | `PROFILE_ID` |
| [EEM_NEWBORN_DETAIL](EEM_NEWBORN_DETAIL.md) | `PROFILE_ID` |
| [EEM_PROFILE_INPUT](EEM_PROFILE_INPUT.md) | `PROFILE_ID` |
| [EEM_PROFILE_LOCATION](EEM_PROFILE_LOCATION.md) | `PROFILE_ID` |
| [EEM_PROFILE_OUTPUT](EEM_PROFILE_OUTPUT.md) | `PROFILE_ID` |
| [EEM_PROFILE_POPULATE](EEM_PROFILE_POPULATE.md) | `PROFILE_ID` |
| [EEM_PROFILE_PRSNL](EEM_PROFILE_PRSNL.md) | `PROFILE_ID` |
| [EEM_PROFILE_REPORT](EEM_PROFILE_REPORT.md) | `PROFILE_ID` |
| [EEM_PROFILE_SCENARIO](EEM_PROFILE_SCENARIO.md) | `PROFILE_ID` |
| [EEM_TRANSACTION](EEM_TRANSACTION.md) | `PROFILE_ID` |

