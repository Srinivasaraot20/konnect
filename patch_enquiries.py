with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/dashboard/enquiries.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the table headers
old_thead = '''                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Mobile</th>
                                <th>Email</th>
                                <th>Location</th>
                                <th>Property Type</th>
                                <th>Status</th>
                                <th>Date</th>
                                <th>Actions</th>
                            </tr>
                        </thead>'''

new_thead = '''                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Mobile</th>
                                <th>Location</th>
                                <th>Property Type</th>
                                <th>Budget</th>
                                <th>Status</th>
                                <th>Submitted Date</th>
                                <th>Last Updated</th>
                                <th>Actions</th>
                            </tr>
                        </thead>'''

html = html.replace(old_thead, new_thead)

# Replace the table body
old_tbody = '''                            <tr>
                                <td>{{ enq.full_name }}</td>
                                <td>{{ enq.mobile_number }}</td>
                                <td>{{ enq.email_address }}</td>
                                <td>{{ enq.preferred_location }}</td>
                                <td>{{ enq.preferred_property_type }}</td>
                                <td>
                                    {% if enq.status == 'New' %}
                                        <span class="badge badge-primary">New</span>
                                    {% elif enq.status == 'Contacted' %}
                                        <span class="badge badge-info">Read</span>
                                    {% else %}
                                        <span class="badge badge-secondary">{{ enq.status }}</span>
                                    {% endif %}
                                </td>
                                <td>{{ enq.enquiry_date|date:"d M Y, h:i A" }}</td>
                                <td>
                                    <button class="btn btn-sm btn-info view-btn" data-id="{{ enq.id }}" data-toggle="modal" data-target="#viewModal" title="View">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                    <button class="btn btn-sm btn-success mark-read-btn" data-id="{{ enq.id }}" title="Mark Read">
                                        <i class="fas fa-check"></i>
                                    </button>
                                    <button class="btn btn-sm btn-secondary mark-replied-btn" data-id="{{ enq.id }}" title="Mark Replied">
                                        <i class="fas fa-reply"></i>
                                    </button>
                                    <button class="btn btn-sm btn-danger delete-btn" data-id="{{ enq.id }}" title="Delete">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                </td>
                            </tr>'''

new_tbody = '''                            <tr>
                                <td>#{{ enq.id }}</td>
                                <td>{{ enq.full_name }}</td>
                                <td>{{ enq.mobile_number }}</td>
                                <td>{{ enq.preferred_location }}</td>
                                <td>{{ enq.preferred_property_type }}</td>
                                <td>{{ enq.budget }}</td>
                                <td>
                                    {% if enq.status == 'New' %}
                                        <span class="badge badge-primary">New</span>
                                    {% elif enq.status == 'Contacted' %}
                                        <span class="badge badge-info">Contacted</span>
                                    {% elif enq.status == 'Follow Up' %}
                                        <span class="badge badge-warning">Follow Up</span>
                                    {% elif enq.status == 'Interested' %}
                                        <span class="badge badge-primary">Interested</span>
                                    {% elif enq.status == 'Site Visit' %}
                                        <span class="badge badge-info">Site Visit</span>
                                    {% elif enq.status == 'Negotiation' %}
                                        <span class="badge badge-warning">Negotiation</span>
                                    {% elif enq.status == 'Sold' %}
                                        <span class="badge badge-success">Sold</span>
                                    {% elif enq.status == 'Not Interested' %}
                                        <span class="badge badge-danger">Not Interested</span>
                                    {% else %}
                                        <span class="badge badge-secondary">{{ enq.status }}</span>
                                    {% endif %}
                                </td>
                                <td>{{ enq.enquiry_date|date:"d M Y" }}</td>
                                <td>{{ enq.last_updated|date:"d M Y" }}</td>
                                <td>
                                    <a href="{% url 'core:dashboard_enquiry_detail' enq.id %}" class="btn btn-sm btn-info" title="View">
                                        <i class="fas fa-eye"></i> View
                                    </a>
                                    <a href="{% url 'core:dashboard_enquiry_edit' enq.id %}" class="btn btn-sm btn-primary" title="Edit">
                                        <i class="fas fa-edit"></i> Edit
                                    </a>
                                </td>
                            </tr>'''

html = html.replace(old_tbody, new_tbody)

# Update filters
old_filters = '''                <div class="col-md-3">
                    <select name="status" class="form-control">
                        <option value="">All Statuses</option>
                        <option value="New" {% if status_filter == 'New' %}selected{% endif %}>New</option>
                        <option value="Contacted" {% if status_filter == 'Contacted' %}selected{% endif %}>Read</option>
                        <option value="Closed" {% if status_filter == 'Closed' %}selected{% endif %}>Closed</option>
                    </select>
                </div>
                <div class="col-md-3">
                    <button type="submit" class="btn btn-primary w-100">Filter</button>
                </div>'''

new_filters = '''                <div class="col-md-3">
                    <select name="status" class="form-control">
                        <option value="">All Statuses</option>
                        <option value="New" {% if status_filter == 'New' %}selected{% endif %}>New</option>
                        <option value="Contacted" {% if status_filter == 'Contacted' %}selected{% endif %}>Contacted</option>
                        <option value="Follow Up" {% if status_filter == 'Follow Up' %}selected{% endif %}>Follow Up</option>
                        <option value="Interested" {% if status_filter == 'Interested' %}selected{% endif %}>Interested</option>
                        <option value="Site Visit" {% if status_filter == 'Site Visit' %}selected{% endif %}>Site Visit</option>
                        <option value="Negotiation" {% if status_filter == 'Negotiation' %}selected{% endif %}>Negotiation</option>
                        <option value="Sold" {% if status_filter == 'Sold' %}selected{% endif %}>Sold</option>
                        <option value="Not Interested" {% if status_filter == 'Not Interested' %}selected{% endif %}>Not Interested</option>
                        <option value="Closed" {% if status_filter == 'Closed' %}selected{% endif %}>Closed</option>
                    </select>
                </div>
                <div class="col-md-3">
                    <select name="date_filter" class="form-control">
                        <option value="">All Time</option>
                        <option value="today" {% if date_filter == 'today' %}selected{% endif %}>Today</option>
                        <option value="yesterday" {% if date_filter == 'yesterday' %}selected{% endif %}>Yesterday</option>
                        <option value="last7" {% if date_filter == 'last7' %}selected{% endif %}>Last 7 Days</option>
                        <option value="last30" {% if date_filter == 'last30' %}selected{% endif %}>Last 30 Days</option>
                        <option value="this_month" {% if date_filter == 'this_month' %}selected{% endif %}>This Month</option>
                    </select>
                </div>
                <div class="col-md-2">
                    <button type="submit" class="btn btn-primary w-100">Search & Filter</button>
                </div>'''

html = html.replace(old_filters, new_filters)
html = html.replace('col-md-6', 'col-md-4')

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/dashboard/enquiries.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated enquiries.html')
