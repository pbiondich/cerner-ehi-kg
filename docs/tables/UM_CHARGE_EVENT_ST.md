# UM_CHARGE_EVENT_ST

> Utilization Management summary table.

**Description:** UM CHARGE EVENT ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 171

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_FORMAT_CD` | DOUBLE | NOT NULL |  | Accession Format Cd |
| 2 | `ACCESSION_NBR` | VARCHAR(50) |  |  | Accession Number of the order. |
| 3 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Activity Subtype cd |
| 4 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of order activity such as 'GLB', 'BB', and 'MICROBIOLOGY'. |
| 5 | `ACT_DRAWN_IN_TRANSIT` | DOUBLE |  |  | Actual Time Drawn to In Transit (In minutes) |
| 6 | `ACT_IN_LAB_PERF` | DOUBLE |  |  | Actual Time In Lab to Performed |
| 7 | `ACT_IN_TRANSIT_IN_LAB` | DOUBLE |  |  | Actual Time In Transit to In Lab |
| 8 | `ACT_ORD_REQ_COLL` | DOUBLE |  |  | Actual Time Ordered to Requested Collection |
| 9 | `ACT_OVERALL_TAT` | DOUBLE |  |  | Actual Time Ordered to Completed |
| 10 | `ACT_PERF_VERIF` | DOUBLE |  |  | Actual Time Performed to Verified |
| 11 | `ACT_REQ_COLL_DRAWN` | DOUBLE |  |  | Actual Time Requested Collection to Drawn |
| 12 | `ACT_VERIF_COMP` | DOUBLE |  |  | Actual Time Verified to Complete |
| 13 | `ADJ_ACT_IN_LAB_PERF` | DOUBLE |  |  | Adjusted Actual time in In Lab to performed |
| 14 | `ADJ_ACT_IN_TRANSIT_IN_LAB` | DOUBLE |  |  | Adjusted Actual time in Transit to In Lab minus weekend minutes. |
| 15 | `ADJ_ACT_ORD_REQ_COLL` | DOUBLE |  |  | Adjusted Actual time in ordered to request collection. |
| 16 | `ADJ_ACT_OVERALL_TAT` | DOUBLE |  |  | Adjusted Actual Time Ordered to Complete minus weekend minutes |
| 17 | `ADJ_ACT_PERF_VERIF` | DOUBLE |  |  | Adjusted Actual time Performed to Verified minus weekend minutes. |
| 18 | `ADJ_ACT_REQ_COLL_DRAWN` | DOUBLE |  |  | Adjusted Actual Time Requested Collection to Drawn Minus Weekend Minutes |
| 19 | `ADJ_ACT_VERIF_COMP` | DOUBLE |  |  | Adjusted Actual Time Verified to Complete minus weekend minutes. |
| 20 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | Microbiology Antibiotic Code |
| 21 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Relates this UM Charge Event to a specific Bill Item |
| 22 | `BILL_QTY` | DOUBLE |  |  | The billed volume for the order/event. |
| 23 | `BILL_REVENUE` | DOUBLE |  |  | The revenue for the order/event. |
| 24 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Microbiology Body Site CD |
| 25 | `CANCEL_DAY` | DOUBLE |  |  | The day of week that the order was cancelled. |
| 26 | `CANCEL_DT_NBR` | DOUBLE |  |  | Cancel date as Julian Date used to join to the omf_date table. |
| 27 | `CANCEL_DT_TM` | DATETIME |  |  | The date/time that the order was cancelled. |
| 28 | `CANCEL_HOUR` | DOUBLE |  |  | The hour of day that the order was cancelled. |
| 29 | `CANCEL_MIN_NBR` | DOUBLE |  |  | Cancel minute number used to join to the omf_time table. |
| 30 | `CANCEL_MONTH` | VARCHAR(10) |  |  | The month in which the order was cancelled. |
| 31 | `CANCEL_QTY` | DOUBLE |  |  | The number of orders that were cancelled. |
| 32 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | The reason that the order was cancelled. |
| 33 | `CASE_INADEQUACY_CD` | DOUBLE | NOT NULL |  | AP Case Inadequacy Cd |
| 34 | `CASE_RESP_PATHOLOGIST_ID` | DOUBLE | NOT NULL |  | AP Case Responsible Pathologist Id |
| 35 | `CASE_RESP_RESIDENT_ID` | DOUBLE | NOT NULL |  | AP Case Responsible Resident Id |
| 36 | `CASE_TYPE_CD` | DOUBLE | NOT NULL |  | AP Case Type Cd |
| 37 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Order Catalog cd |
| 38 | `CHARGE_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identification number for the charge. |
| 39 | `CLIENT_CLASS_CD` | DOUBLE | NOT NULL |  | Grouping of organizations. |
| 40 | `CLIENT_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of organizations. |
| 41 | `CLIENT_ID` | DOUBLE | NOT NULL | FK→ | The organization id for the order. |
| 42 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | Collection Method |
| 43 | `COLL_PRIOR_CD` | DOUBLE | NOT NULL |  | The collection priority assigned to the order. |
| 44 | `COLL_PRIOR_GRP_CD` | DOUBLE | NOT NULL |  | The grouping of collection priorities to which the collectionpriority assigned to the order belongs. |
| 45 | `COMP_DAY` | DOUBLE |  |  | The day of week that the order was completed. |
| 46 | `COMP_DT_NBR` | DOUBLE |  |  | Complete date as Julian date, used to join to the omf_date table |
| 47 | `COMP_DT_TM` | DATETIME |  |  | The date and time that the order was completed. |
| 48 | `COMP_HOUR` | DOUBLE |  |  | The hour of day that the order was completed. |
| 49 | `COMP_MIN_NBR` | DOUBLE |  |  | Complete minute number used to join to the omf_time table |
| 50 | `COMP_MONTH` | VARCHAR(10) |  |  | The month of year that the order was completed. |
| 51 | `COMP_QTY` | DOUBLE |  |  | Set to 1 when the order is completed; otherwise 0. |
| 52 | `COMP_SHIFT_CD` | DOUBLE | NOT NULL |  | The shift grouping for the order based on completed date and time. |
| 53 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 54 | `CREDITED_QTY` | DOUBLE |  |  | The number of orders that were credited. |
| 55 | `CREDITED_REVENUE` | DOUBLE |  |  | The amount of revenue associated with the credited qty. |
| 56 | `CULTURE_DT_NBR` | DOUBLE |  |  | Microbiology Culture Start date as Julian date, used to join to the omf_date table |
| 57 | `CULTURE_DT_TM` | DATETIME |  |  | Microbiology Culture Start dt/tm |
| 58 | `CULTURE_MIN_NBR` | DOUBLE |  |  | Microbiology Culture Start time in minutes from start of the day used for omf_time functions. |
| 59 | `CULTURE_SHIFT_CD` | DOUBLE | NOT NULL |  | Microbiology Culture Start Shift |
| 60 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | The department to which the order loaded. |
| 61 | `DETAIL_IND` | DOUBLE | NOT NULL |  | Set to 1 if the record is at the detail level, 0 if the record is at the order level. |
| 62 | `DRAWN_DAY` | DOUBLE |  |  | The day of week that the order was collected. |
| 63 | `DRAWN_DT_NBR` | DOUBLE |  |  | Date Drawn as Julian Date, used to join to omf_date table. |
| 64 | `DRAWN_DT_TM` | DATETIME |  |  | The date and time that the order was collected. |
| 65 | `DRAWN_HOUR` | DOUBLE |  |  | The hour of day in which the order was collected. |
| 66 | `DRAWN_MIN_NBR` | DOUBLE |  |  | Drawn minute number, used to join to omf_time table. |
| 67 | `DRAWN_MONTH` | VARCHAR(10) |  |  | The month of year in which the order was collected. |
| 68 | `DRAWN_SHIFT_CD` | DOUBLE | NOT NULL |  | The shift grouping for the order based on the collected date and time. |
| 69 | `DRAWN_TECH_ID` | DOUBLE | NOT NULL |  | Drawing technician(Phlebotomist) id. |
| 70 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 71 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The encounter type code assigned to the patient for the order. |
| 72 | `ENCNTR_TYPE_GRP_CD` | DOUBLE | NOT NULL |  | The encounter type grouping to which the encounter type code belongs for the order. |
| 73 | `EXP_DRAWN_IN_TRANSIT` | DOUBLE |  |  | Expected time drawn to in transit |
| 74 | `EXP_IN_LAB_PERF` | DOUBLE |  |  | Expected time in lab to performed |
| 75 | `EXP_IN_TRANSIT_IN_LAB` | DOUBLE |  |  | Expected time in transit to in lab |
| 76 | `EXP_ORD_REQ_COLL` | DOUBLE |  |  | Expected time ordered to requested collection |
| 77 | `EXP_OVERALL_TAT` | DOUBLE |  |  | Expected time ordered to completed |
| 78 | `EXP_PERF_VERIF` | DOUBLE |  |  | Expected time performed to verified |
| 79 | `EXP_REQ_COLL_DRAWN` | DOUBLE |  |  | Expected time requested collection to drawn |
| 80 | `EXP_VERIF_COMP` | DOUBLE |  |  | Expected time verified to complete |
| 81 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | The encounter's financial class. |
| 82 | `ICD9_NOMEN_ID` | DOUBLE | NOT NULL |  | ICD9 primary diagnosis ** for the detail procedure **. This is gotten from the Charge_mode table. |
| 83 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | The institution to which the order loaded. |
| 84 | `IN_LAB_DAY` | DOUBLE |  |  | The day of week that the order was received in lab. |
| 85 | `IN_LAB_DT_NBR` | DOUBLE |  |  | Received Date as Julian Date, used to join to omf_date table. |
| 86 | `IN_LAB_DT_TM` | DATETIME |  |  | The date and time at which the order reached in lab status. |
| 87 | `IN_LAB_HOUR` | DOUBLE |  |  | The hour of day in which the order reached in lab status. |
| 88 | `IN_LAB_MIN_NBR` | DOUBLE |  |  | Received minute number, used to join to omf_time table. |
| 89 | `IN_LAB_MONTH` | VARCHAR(10) |  |  | The month of year in which the order reached in lab status. |
| 90 | `IN_LAB_SHIFT_CD` | DOUBLE | NOT NULL |  | The shift grouping for the order based on in lab date and time. |
| 91 | `IN_TRANSIT_DAY` | DOUBLE |  |  | The day of week that the order went in transit. |
| 92 | `IN_TRANSIT_DT_TM` | DATETIME |  |  | The date and time in which the order went in transit. |
| 93 | `IN_TRANSIT_HOUR` | DOUBLE |  |  | The hour of day in which the order went in transit. |
| 94 | `IN_TRANSIT_MONTH` | VARCHAR(10) |  |  | The month of year in which the order went in transit. |
| 95 | `IN_TRANSIT_SHIFT_CD` | DOUBLE | NOT NULL |  | The shift grouping for the order based on in transit date and time. |
| 96 | `MED_SPEC_CD` | DOUBLE | NOT NULL |  | The medical specialty grouping for the order based on ordering physician. |
| 97 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | Type of order from the Orders table. This will tell us, for example, whether this order is a care set and thus should not be counted in volume views. |
| 98 | `ORDER_DT_TM` | DATETIME |  |  | The date and time at which the order took place. |
| 99 | `ORDER_ID` | DOUBLE | NOT NULL |  | The unique identification number for the order. |
| 100 | `ORDER_NU_CD` | DOUBLE | NOT NULL |  | Nurse Unit from which the order was placed. |
| 101 | `ORDER_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | Ordering physician group (as set in the OMF Grouping Tool). |
| 102 | `ORDER_PHYS_ID` | DOUBLE | NOT NULL |  | Ordering physicianid. |
| 103 | `ORDER_QTY` | DOUBLE |  |  | Quantity of the order. |
| 104 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | Order status code value such as 'CANCELED' and 'COMPLETED'. |
| 105 | `ORD_DAY` | DOUBLE |  |  | The day of week that the order took place. |
| 106 | `ORD_DT_NBR` | DOUBLE |  |  | Date Ordered as Julian Date, used to join to omf_date table. |
| 107 | `ORD_HOUR` | DOUBLE |  |  | Hour (0 to 23) procedure was ordered. |
| 108 | `ORD_MIN_NBR` | DOUBLE |  |  | Ordered time minute number used to join to omf_time table. |
| 109 | `ORD_MONTH` | VARCHAR(10) |  |  | Month (1 to 12) the procedure was ordered. |
| 110 | `ORD_SHIFT_CD` | DOUBLE | NOT NULL |  | Shift the procedure was ordered (as defined in the OMF Grouping Tool). |
| 111 | `ORD_YEAR` | DOUBLE |  |  | Year the procedure was ordered. |
| 112 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | Organism |
| 113 | `PARENT_BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Parent of this bill item (e.g. for a detail procedure its the ordered procedure, for an order procedure its the order procedure again or a care set id) |
| 114 | `PATIENT_BUILD_CD` | DOUBLE | NOT NULL |  | Building where the patient was located when the order was placed. |
| 115 | `PATIENT_FAC_CD` | DOUBLE | NOT NULL |  | Facility where the patient was located when the order was placed. |
| 116 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | Person id of patient |
| 117 | `PATIENT_NU_CD` | DOUBLE | NOT NULL |  | Patient nurse unit (when procedure was ?ordered?). |
| 118 | `PATIENT_NU_GRP_CD` | DOUBLE | NOT NULL |  | Patient nurse unit group (when procedure was ordered?) as defined in OMF Grouping Tool. |
| 119 | `PERF_DAY` | DOUBLE |  |  | The day of week that the detail was performed. |
| 120 | `PERF_DT_NBR` | DOUBLE |  |  | Date Performed as Julian Date, used to join to omf_date table. |
| 121 | `PERF_DT_TM` | DATETIME |  |  | Performing date and time. |
| 122 | `PERF_HOUR` | DOUBLE |  |  | Performing hour of day (0 to 23). |
| 123 | `PERF_MIN_NBR` | DOUBLE |  |  | Performed time minute number used to join to omf_time table. |
| 124 | `PERF_MONTH` | VARCHAR(10) |  |  | Performing month (1 to 12). |
| 125 | `PERF_QTY` | DOUBLE |  |  | Set to 1 when result/task is performed |
| 126 | `PERF_SHIFT_CD` | DOUBLE | NOT NULL |  | Performing shift (as defined in OMF Grouping Tool). |
| 127 | `PERF_TECH_ID` | DOUBLE | NOT NULL |  | Person Id of Tech who performed the result |
| 128 | `REFERENCE_NBR` | VARCHAR(255) | NOT NULL |  | Reference number of this row (e.g. for Gen Lab and Blood Bank this is order_id, result_id, task_assay_cd). |
| 129 | `REQ_COLL_DAY` | DOUBLE |  |  | The day of week that the collection was requested. |
| 130 | `REQ_COLL_DT_NBR` | DOUBLE |  |  | Requested Collection Date as Julian Date, used to join to omf_date table. |
| 131 | `REQ_COLL_DT_TM` | DATETIME |  |  | Requested collection date and time. |
| 132 | `REQ_COLL_HOUR` | DOUBLE |  |  | Requested collection hour of day (0 to 23). |
| 133 | `REQ_COLL_MIN_NBR` | DOUBLE |  |  | Requested collection time minute number used to join to omf_time table. |
| 134 | `REQ_COLL_MONTH` | VARCHAR(10) |  |  | Requested collection month (1 to 12). |
| 135 | `REQ_COLL_SHIFT_CD` | DOUBLE | NOT NULL |  | Request collection shift (as defined in the OMF Grouping Tool). |
| 136 | `RESULT_ID` | DOUBLE | NOT NULL |  | Id from the result table or mic_task_log table |
| 137 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Detail procedure result status such as 'verified', 'corrected', etc. |
| 138 | `RPT_PRIOR_CD` | DOUBLE | NOT NULL |  | Report Priority Code form Order_laboratory |
| 139 | `RULE_ID` | DOUBLE | NOT NULL |  | ID of Turnaround Time Rule that this order qualified for |
| 140 | `SECTION_CD` | DOUBLE | NOT NULL |  | Ordering? Section. |
| 141 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Service resource were action was perfomed. |
| 142 | `SITE_PREFIX_CD` | DOUBLE | NOT NULL |  | Accession Site Prefix Cd |
| 143 | `SMR_FLAG` | DOUBLE |  |  | Data level setting for Standard Mgmt when this row was populated. |
| 144 | `SM_FLAG` | DOUBLE |  |  | Data level setting for Service Mgmt when this row was populated. |
| 145 | `SPECIMEN_CD` | DOUBLE | NOT NULL |  | AP Specimen Cd |
| 146 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Specimen Type |
| 147 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | Subsection where action was performed. |
| 148 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task or Discrete Assay |
| 149 | `TASK_DETAIL_CD` | DOUBLE | NOT NULL |  | Microbiology Panel or Detail Biochemical |
| 150 | `TASK_TYPE_FLAG` | DOUBLE |  |  | Micro Task Type |
| 151 | `TAT_QUAL_IND` | DOUBLE |  |  | 1 = Qualified for a turnaround time rule |
| 152 | `TSK_ORD_DT_NBR` | DOUBLE |  |  | Task Order Date as Julian date used for OMF_Date functions. |
| 153 | `TSK_ORD_DT_TM` | DATETIME |  |  | Task Order Dt/Tm |
| 154 | `TSK_ORD_MIN_NBR` | DOUBLE |  |  | Task Order Time in minutes used for OMF_time functions. |
| 155 | `TSK_ORD_SHIFT_CD` | DOUBLE | NOT NULL |  | Task Order Time Shift |
| 156 | `UM_CHARGE_EVENT_ST_ID` | DOUBLE | NOT NULL |  | Unique identifier for table. Only used because true key has 3 elements (order_id, reference_nbr, contributor_system_cd) but this is not allowed for combines. |
| 157 | `UM_FLAG` | DOUBLE |  |  | Data level setting for Utilization Mgmt when this row was populated. |
| 158 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 159 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 160 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 161 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 162 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 163 | `VERIF_DAY` | DOUBLE |  |  | The day of week that the detail was verified. |
| 164 | `VERIF_DT_NBR` | DOUBLE |  |  | Verified date as Julian date used to join to omf_time table. |
| 165 | `VERIF_DT_TM` | DATETIME |  |  | Verfied date and time. |
| 166 | `VERIF_HOUR` | DOUBLE |  |  | Verified hour of day (0 to 23). |
| 167 | `VERIF_MIN_NBR` | DOUBLE |  |  | Verfied time minute number used to join to omf_time table. |
| 168 | `VERIF_MONTH` | VARCHAR(10) |  |  | Verified month (1 to 12). |
| 169 | `VERIF_QTY` | DOUBLE |  |  | The quantity verified. |
| 170 | `VERIF_SHIFT_CD` | DOUBLE | NOT NULL |  | Verified shift (as defined in OMF Grouping Tool). |
| 171 | `VERIF_TECH_ID` | DOUBLE | NOT NULL |  | Verified Technician Person ID |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `CHARGE_EVENT_ID` | [CHARGE_EVENT](CHARGE_EVENT.md) | `CHARGE_EVENT_ID` |
| `CLIENT_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PARENT_BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

